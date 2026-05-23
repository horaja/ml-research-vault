# Variational Spatial Prior for Multimodal Patch Selection

> Deep dive into a latent-variable formulation of Module 1, where a language-conditioned prior and image-refined posterior jointly learn a spatial attention map over image patches, trained end-to-end via the ELBO.

---

## 1. Motivation

The core problem: given a language instruction $l$ and a high-resolution image $x$ decomposed into $N$ patches, produce a spatial attention map $z \in \mathbb{R}^N$ that identifies which patches are task-relevant—before the expensive downstream ViT and policy network ever see them.

A discriminative scorer (e.g., energy-based or contrastive) can do this, but it treats patch selection as a point estimate: each patch gets a single relevance score. This leaves three things on the table:

1. **No standalone language prior.** A discriminative scorer needs the image to produce scores. There's no mechanism to predict "where to look" from the instruction alone, which means the first pass of an iterative architecture has nothing to work with.
2. **No calibrated uncertainty.** A scalar score doesn't tell you how *confident* the model is about a patch's relevance. You need a separate uncertainty predictor (Module 3) to decide when to re-select.
3. **No regularization against degenerate attention.** Without structural constraints, the scorer can collapse to always selecting the same patches or ignoring the language entirely.

The variational formulation addresses all three by introducing a latent variable $z$ with an explicit prior-posterior structure.

---

## 2. The Generative Story

Every probabilistic model starts with a story about how the data was generated. For our problem:

1. A language instruction $l$ arrives (e.g., "pick up the red cup").
2. Before seeing the image, the instruction alone induces a **spatial prior** over where task-relevant content is likely to be. This is $p_\theta(z \mid l)$.
3. The actual image $x$ arrives, and the prior is **refined** into a posterior. This is $q_\phi(z \mid x, l)$, incorporating what's actually in the scene.
4. The attention map $z$ selects patches, and selected patches feed into the downstream policy to predict actions $a$.

The key conceptual move: $z$ is a **latent variable** that mediates between the instruction and patch selection. It is not directly observed during training—you never have ground-truth "perfect attention maps" (unless you use DAA gaze data, addressed in §7). Instead, $z$ is inferred from the quality of downstream action prediction.

---

## 3. Formal Setup

### Notation

| Symbol | Meaning |
|---|---|
| $x$ | Full image, decomposed into $N$ patches $\{x_1, \ldots, x_N\}$ |
| $l$ | Language instruction embedding |
| $z \in \mathbb{R}^N$ | Spatial attention logits; $z_i$ = importance logit for patch $i$ |
| $\alpha \in \Delta^{N-1}$ | Attention weights after softmax: $\alpha = \mathrm{softmax}(z / \tau)$ |
| $v_i$ | Embedding of patch $i$ (from line drawing features, pixels, or frozen encoder) |
| $a$ | Action output from the downstream policy |
| $\tau$ | Temperature controlling selection sharpness |

### Generative Model (Decoder)

$$p_\theta(a \mid x, l) = \int p_\theta(a \mid x_{\mathrm{selected}}, l) \cdot p_\theta(z \mid l) \, dz$$

where $x_{\mathrm{selected}}$ is the set of patches selected according to $z$. This integral is intractable—you cannot enumerate all possible attention maps—so you introduce a variational posterior $q_\phi(z \mid x, l)$ to approximate the true posterior $p(z \mid x, l, a)$ and optimize the ELBO.

---

## 4. The ELBO

The evidence lower bound for a single training example $(x, l, a)$ is:

$$\mathcal{L}_{\mathrm{ELBO}} = \underbrace{\mathbb{E}_{z \sim q_\phi(z \mid x, l)} \big[ \log p_\theta(a \mid \mathrm{select}(x, z), l) \big]}_{\text{Reconstruction: action prediction quality}} - \underbrace{D_{\mathrm{KL}}\big( q_\phi(z \mid x, l) \;\|\; p_\theta(z \mid l) \big)}_{\text{Regularizer: posterior must match prior}}$$

### Term 1: Reconstruction

Sample an attention map $z$ from the posterior, select patches accordingly, run the policy, and measure how well it predicts the correct action. This is the existing action prediction loss, computed on variably-selected patches rather than fixed ones.

### Term 2: KL Regularizer

Forces the posterior ("where to look given image + instruction") to stay close to the prior ("where to look given only the instruction"). Maximizing the ELBO means: find attention maps that support good action prediction (Term 1) while being predictable from the instruction alone (Term 2).

### What the KL Term Does

Three concrete effects:

1. **Forces language to carry spatial information.** Without KL, the model can ignore language and use visual saliency alone. The KL term penalizes posterior attention maps that diverge from the language-only prior. If the posterior attends to a specific region, the prior must also predict that region from the instruction alone.
2. **Regularizes against degenerate attention.** If the posterior collapses to always selecting the same patches, the KL penalty explodes because the prior cannot explain constant behavior from varying instructions.
3. **Produces a usable language-only prior at test time.** Once trained, $p_\theta(z \mid l)$ alone generates an initial attention map before seeing the image—directly powering the first pass of an iterative coarse-to-fine loop.

---

## 5. Network Architecture

### 5.1 Prior Network $p_\theta(z \mid l)$

Takes only the language embedding as input. Outputs parameters of a distribution over the $N$-dimensional patch grid.

**Minimal version (independent Gaussians):**

```
l_embed = frozen_text_encoder(instruction)          # e.g., DeCLUTR, dim 384
h       = MLP(l_embed, hidden=[256, 256])            # 2-3 layers
μ_prior       = Linear(h) → ℝ^N                     # mean logit per patch
log_σ_prior   = Linear(h) → ℝ^N                     # log-variance per patch
```

Output: $p(z_i \mid l) = \mathcal{N}(\mu_{\mathrm{prior},i},\; \sigma_{\mathrm{prior},i}^2)$ independently per patch.

To get an attention map: $\alpha = \mathrm{softmax}(z / \tau)$ after sampling.

**Why independent Gaussians?** The patch grid has spatial structure that the prior should eventually learn (nearby patches should be correlated), but independent Gaussians let the MLP learn correlations implicitly through shared hidden layers. Simpler to implement, stable to train.

**Richer version (2D Gaussian mixture model):**

```
l_embed = frozen_text_encoder(instruction)
# Predict K-component 2D Gaussian mixture over the image plane
π, μ_xy, Σ_xy = GMM_head(MLP(l_embed))     # K weights, K 2D means, K 2D covariances

# Render the mixture onto the patch grid
z_prior_i = Σ_k  π_k · N(patch_center_i; μ_xy_k, Σ_xy_k)
```

With $K = 3\text{–}5$ components, this handles most manipulation tasks (one component per task-relevant object). The mixture means are interpretable as "predicted locations of task-relevant objects." This version has a much stronger spatial inductive bias and would make a compelling visualization in a paper.

**When to upgrade:** Start with the independent Gaussian version. If the prior's attention maps look spatially incoherent (scattered, non-smooth), switch to the GMM version.

### 5.2 Posterior Network $q_\phi(z \mid x, l)$

Takes both image patches and language embedding. Outputs a refined distribution.

```
# Embed each patch
v_i  = patch_encoder(x_i)                           # small CNN or ViT patch embed
ld_i = line_drawing_features(x_i)                   # edge density, contour overlap, etc.
v_i  = concat(v_i, ld_i)                            # augment with biological features

# Cross-modal scoring
l_embed = frozen_text_encoder(instruction)
s_i     = MLP(concat(v_i, l_embed, v_i ⊙ l_embed)) # per-patch relevance score
                                                      # ⊙ = Hadamard product

# Output posterior parameters
μ_post_i       = s_i                                 # mean logit for patch i
log_σ_post_i   = Linear(s_i)                         # learned variance per patch
```

The posterior is richer than the prior because it sees the actual image—it knows where the red cup *is*, not just where cups tend to be. The variance $\sigma_{\mathrm{post},i}$ captures uncertainty: high variance on a patch means "I'm not sure this patch matters."

**The Hadamard product $v_i \odot l_{\mathrm{embed}}$** captures multiplicative feature-level interactions. Concatenation alone only lets the MLP learn additive relationships. The element-wise product lets features "gate" each other—e.g., a language feature for "red" can amplify the visual feature for color channels.

### 5.3 Design Choices for Patch Embeddings $v_i$

The input to the posterior. Three options with different tradeoffs:

| Option | Description | Pros | Cons |
|---|---|---|---|
| **(a)** Small CNN on line drawing patches | 3–4 conv layers on the line drawing crop | Independent of downstream ViT; avoids circular dependency flagged in Overview.md | Limited representational power |
| **(b)** ViT patch embedding layer | Linear projection from pixels to tokens, reusing the downstream ViT's first layer | Minimal parameters; shared representation | Couples Module 1 to the ViT backbone |
| **(c)** Frozen encoder (DINOv2) on original patches | Rich pre-trained features | Most powerful features | Adds inference cost from frozen forward pass |

**Recommendation:** Start with **(a)** for the prototype—keeps Module 1 fully independent and avoids the circular dependency your Overview.md flags (prior cannot depend on representations computed from selected patches). Upgrade to **(c)** if **(a)**'s representational capacity proves insufficient.

---

## 6. Reparameterization and Patch Selection

### 6.1 Reparameterization Trick

You cannot backpropagate through sampling. The reparameterization trick makes sampling differentiable:

```
ε ~ N(0, I)                                         # sample standard normal noise
z = μ_post + σ_post ⊙ ε                             # deterministic function of params + noise
α = softmax(z / τ)                                  # attention weights
```

Gradients now flow through $\mu_{\mathrm{post}}$ and $\sigma_{\mathrm{post}}$ to the posterior network.

### 6.2 Soft Selection (Training)

During training, weight each patch embedding by its attention weight:

$$\hat{v} = \sum_{i=1}^{N} \alpha_i \cdot v_i$$

Or, for a richer representation, pass all patch embeddings weighted by $\alpha$ into the downstream ViT (i.e., scale each token's contribution by its attention weight). All patches get processed—no efficiency gain during training—but the attention map is fully differentiable.

### 6.3 Hard Selection (Inference)

At inference, take the top-$k$ patches by $\alpha$, discard the rest. This is where computational savings materialize.

**Bridging the soft-hard gap.** The discrepancy between soft training and hard inference is a known issue. Mitigations:

1. **Temperature annealing:** Decrease $\tau$ during training to make softmax sharper, approaching hard selection.
2. **Straight-through Gumbel-softmax:** Hard selections in the forward pass, soft gradients in the backward pass.
3. **Perturbed top-$k$ (Berthet et al., 2020):** Differentiable top-$k$ operator using random perturbations.

**Recommendation:** Start with soft selection + temperature annealing. Switch to Gumbel-softmax only if the soft-hard gap causes significant performance degradation at inference.

---

## 7. Training Procedure

### 7.1 Core ELBO Training

```python
for each batch (x, l, a) from BEHAVIOR-1K demonstrations:

    # 1. Compute posterior parameters
    μ_post, σ_post = posterior_net(patches(x), l)

    # 2. Compute prior parameters
    μ_prior, σ_prior = prior_net(l)

    # 3. Sample attention map via reparameterization
    ε ~ N(0, I)
    z = μ_post + σ_post ⊙ ε
    α = softmax(z / τ)

    # 4. Select/weight patches
    weighted_patches = Σ_i α_i · v_i          # soft selection during training

    # 5. Run downstream policy on selected patches
    â = policy(weighted_patches, l)

    # 6. Compute ELBO loss
    L_recon = action_loss(â, a)               # MSE, diffusion loss, etc.
    L_KL    = Σ_i [ log(σ_prior_i / σ_post_i)
                   + (σ_post_i² + (μ_post_i − μ_prior_i)²) / (2 σ_prior_i²)
                   − 1/2 ]

    L_total = L_recon + β · L_KL

    # 7. Backprop through everything
    optimizer.step()
```

### 7.2 The β Coefficient

The weight on the KL term is **critical**. This is the β-VAE knob:

| β too high | β too low |
|---|---|
| Posterior collapse: $q \approx p$, $z$ carries no image information, attention map is pure function of language | Prior never learns: $z$ becomes deterministic function of image, no regularization, prior is useless at test time |
| Symptom: KL → 0 early, reconstruction plateaus at mediocre level | Symptom: KL stays permanently high, prior maps look uniform |

**Practical schedule:**

1. **KL-free warmup** (epochs 1–K): Train with $\beta = 0$. Let the posterior learn useful attention from the reconstruction loss alone.
2. **Linear annealing** (epochs K–2K): Increase $\beta$ from 0 to target value (e.g., 0.01–0.1).
3. **Stable training** (epochs 2K+): Hold $\beta$ at target, monitor KL and reconstruction jointly.

**Free bits (Kingma et al., 2016):** Only penalize KL when it exceeds a minimum value $\lambda$ per dimension:

$$\hat{L}_{\mathrm{KL}} = \sum_i \max(\mathrm{KL}_i, \lambda)$$

This prevents posterior collapse by ensuring each latent dimension carries at least $\lambda$ nats of information.

### 7.3 KL Balancing (from HULC)

The prior only receives gradient through the KL term, not the reconstruction loss. If $\beta$ is low, the prior trains very slowly while the posterior races ahead. Use **asymmetric learning rates within the KL gradient**:

- Prior update: scale KL gradient by $\alpha_{\mathrm{prior}} = 0.8$ (faster)
- Posterior update: scale KL gradient by $1 - \alpha_{\mathrm{prior}} = 0.2$ (slower)

This ensures the prior is pulled toward the posterior more aggressively than the posterior is pulled toward the prior.

---

## 8. Incorporating DAA Gaze Supervision

The DAA dataset (Kim et al., 2024) provides human gaze coordinates during manipulation demonstrations—direct spatial supervision for "where a human looked given this instruction."

### 8.1 Gaze Loss Formulation

For training examples that have gaze annotations $(g_x, g_y)$:

```python
# Create soft gaze target over patch grid
gaze_target = gaussian_kernel(patch_centers, (gx, gy), σ=gaze_spread)
gaze_target = gaze_target / gaze_target.sum()       # normalize to distribution

# Supervise both prior and posterior
L_gaze_prior = KL(gaze_target ‖ softmax(μ_prior / τ))
L_gaze_post  = KL(gaze_target ‖ softmax(μ_post / τ))

L_total = L_recon + β · L_KL + γ · (L_gaze_prior + L_gaze_post)
```

### 8.2 Why Supervise the Prior?

The gaze loss on $p_\theta(z \mid l)$ is especially valuable: it directly teaches the language-only network "for this instruction, a human would look here." This accelerates prior learning far beyond what the KL term alone can achieve.

### 8.3 Cross-Dataset Training

DAA gaze data and BEHAVIOR-1K demonstrations come from different distributions. Training scheme:

| Loss | Computed on |
|---|---|
| $L_{\mathrm{recon}}$ (action prediction) | BEHAVIOR-1K examples only |
| $L_{\mathrm{KL}}$ (prior-posterior alignment) | All examples |
| $L_{\mathrm{gaze}}$ (gaze supervision) | DAA examples only |

The KL term bridges the two datasets by forcing a shared latent structure: the prior must be consistent across both domains.

### 8.4 Gripper-Close Heuristic (from HULC++)

As a supplementary supervision signal on BEHAVIOR-1K data (where gaze is unavailable): wherever the gripper closes during a demonstration, that patch was task-relevant. This provides a second source of spatial supervision, directly in your target domain:

```python
# For BEHAVIOR-1K examples with gripper-close events at (ee_x, ee_y):
ee_target = gaussian_kernel(patch_centers, (ee_x, ee_y), σ=ee_spread)
ee_target = ee_target / ee_target.sum()
L_ee = KL(ee_target ‖ softmax(μ_post / τ))
```

This is noisier than gaze but free and domain-matched.

---

## 9. Integration with the Iterative Architecture

The variational formulation connects naturally to the iterative coarse-to-fine loop in the full system architecture:

### Pass 1: Language-Only Prior

Use $p_\theta(z \mid l)$ to select patches without seeing the image. Run the policy. Compute action-level uncertainty.

- **What this achieves:** A fast, cheap initial guess. "Pick up the red cup" → attend to the central workspace area where objects typically sit.
- **What powers it:** The trained prior, shaped by KL regularization and (optionally) gaze supervision.

### Pass 2: Image-Refined Posterior

If uncertainty exceeds threshold, compute the posterior $q_\phi(z \mid x, l)$. The posterior refines the prior's selection—it shifts attention to where the red cup actually is. Re-run the policy on updated patches.

- **What this achieves:** Correction of the prior's mistakes using actual visual evidence.
- **Computational note:** The posterior requires a forward pass through the patch encoder and cross-modal scoring MLP, but this is far cheaper than the downstream ViT+policy.

### Pass 3: Uncertainty-Guided Refinement

If uncertainty remains high, the posterior variance $\sigma_{\mathrm{post}}$ provides a spatial uncertainty map. Patches with high $\sigma_{\mathrm{post},i}$ are where the model is unsure about relevance. Select additional patches specifically from high-variance regions.

- **What this achieves:** Targeted refinement—don't re-examine everything, only the uncertain regions.
- **Key insight:** $\sigma_{\mathrm{post}}$ replaces the need for a separate Module 3 uncertainty predictor for spatial attention. Module 3 can focus on action-level uncertainty (from the diffusion head), while spatial uncertainty is handled natively by the posterior.

---

## 10. Failure Modes and Mitigations

### 10.1 Posterior Collapse

**What happens:** KL dominates; posterior matches prior exactly; $z$ carries no image information; attention map becomes a pure function of language.

**Detection:** KL loss → ~0 early in training; reconstruction loss plateaus.

**Mitigations:**
- Low initial β with annealing (§7.2)
- KL-free warmup period
- Free bits threshold
- Richer posterior architecture (give it more capacity to diverge from prior)

### 10.2 Prior Underfitting

**What happens:** Prior network is too weak to match the posterior; KL stays permanently high; prior attention maps look uniform.

**Detection:** KL loss remains high after extensive training; prior outputs ≈ uniform distribution.

**Mitigations:**
- Larger prior MLP or switch to GMM parameterization
- Richer language encoder (CLIP text encoder instead of DeCLUTR)
- Gaze auxiliary loss to give prior direct supervision
- KL balancing with asymmetric learning rates

### 10.3 Mode Collapse in Attention

**What happens:** Posterior always attends to a single patch or fixed set regardless of instruction (e.g., center of table is always action-relevant).

**Detection:** Low entropy in attention maps across diverse instructions; attention variance across dataset is low.

**Mitigations:**
- Entropy regularization: penalize $-H(\alpha) = \sum_i \alpha_i \log \alpha_i$ when it falls below a threshold
- KL term partially prevents this (prior can't predict constant attention from diverse instructions)
- Data augmentation: random spatial transforms to prevent spatial bias

### 10.4 Gaze-Language Decorrelation

**What happens:** DAA gaze data was collected without true language conditioning—demonstrators look at the same object regardless of instruction phrasing. The language branch of the posterior gets no gradient.

**Detection:** Mutual information between language features and posterior attention is near zero; ablating the language input doesn't change attention maps.

**Diagnostic:** For the same scene with different instructions, do DAA gaze patterns differ? If not, the gaze supervision cannot teach language-conditioned attention.

**Mitigation:** Rely on the ELBO reconstruction loss (which *is* language-conditioned) to learn language-attention coupling; use gaze loss only for initializing spatial structure.

### 10.5 Circular Dependency

**What happens:** If the posterior's input includes features computed from the selected patches, gradients create a feedback loop within a single forward pass.

**Hard rule:** The posterior must only see: (1) the line drawing (computed independently of patch selection), (2) raw patch embeddings (from a frozen or independent encoder), and (3) the language embedding (exogenous). Never feed selected-patch features back into Module 1 within a single forward pass.

---

## 11. Implementation Plan (Summer Timeline)

| Week | Milestone | Deliverable |
|---|---|---|
| 1–2 | Posterior only (no prior, no KL) | Working language-conditioned patch scorer; ablate against line-drawing-only baseline |
| 3 | Add prior + KL loss | Full Architecture C; verify prior is training (attention maps become instruction-specific) |
| 4 | Add gaze supervision | DAA gaze loss on prior + posterior; measure convergence speedup |
| 5–6 | Integrate with iterative refinement | Prior → Pass 1, Posterior → Pass 2, σ_post → Pass 3; connect Module 1 to Module 3 |
| 7–8 | Evaluation on BEHAVIOR-1K | Full benchmark; compare against task-agnostic line-drawing baseline; correlation with human gaze (Option B from Overview.md) |

Each stage is independently useful. If anything breaks, fall back to the previous working stage.

---

## 12. Relation to Prior Work

| Method | Relation to Architecture C |
|---|---|
| **Yang et al. (2020)** – Soft Modularization | Routes over *computational paths*, not *spatial locations*. Wrong output topology for patch selection. Architecture C directly produces spatial attention maps. |
| **Kim et al. (2024)** – DAA | Provides gaze supervision signal. Architecture C's prior network is conceptually analogous to DAA's gaze predictor, but trained variational rather than supervised. |
| **Mees et al. (2023)** – HULC++ | Produces language-conditioned spatial heatmaps via supervised classification (cross-entropy on projected end-effector). Architecture C generalizes this to a variational formulation with explicit prior/posterior separation. |
| **TRIPS (2023)** | Text-guided patch selection for VLP models. Discriminative (no prior/posterior split, no uncertainty). Architecture C adds the variational layer on top of a similar selection mechanism. |
| **β-VAE (Higgins et al., 2017)** | Foundational framework. Architecture C applies β-VAE principles to *spatial attention* rather than *image generation*. |

---

## 13. Key Equations Summary

**ELBO:**
$$\mathcal{L} = \mathbb{E}_{z \sim q_\phi} \big[ \log p_\theta(a \mid \mathrm{select}(x,z), l) \big] - \beta \cdot D_{\mathrm{KL}}(q_\phi \| p_\theta)$$

**Gaussian KL (closed-form):**
$$D_{\mathrm{KL}} = \sum_{i=1}^{N} \left[ \log \frac{\sigma_{\mathrm{prior},i}}{\sigma_{\mathrm{post},i}} + \frac{\sigma_{\mathrm{post},i}^2 + (\mu_{\mathrm{post},i} - \mu_{\mathrm{prior},i})^2}{2\sigma_{\mathrm{prior},i}^2} - \frac{1}{2} \right]$$

**Reparameterization:**
$$z = \mu_{\mathrm{post}} + \sigma_{\mathrm{post}} \odot \varepsilon, \quad \varepsilon \sim \mathcal{N}(0, I)$$

**Attention weights:**
$$\alpha_i = \frac{\exp(z_i / \tau)}{\sum_j \exp(z_j / \tau)}$$

**Gaze auxiliary loss:**
$$\mathcal{L}_{\mathrm{gaze}} = D_{\mathrm{KL}}\big( \mathrm{gaze\_target} \;\|\; \mathrm{softmax}(\mu / \tau) \big)$$

**Total training loss:**
$$\mathcal{L}_{\mathrm{total}} = \mathcal{L}_{\mathrm{recon}} + \beta \cdot \mathcal{L}_{\mathrm{KL}} + \gamma \cdot \mathcal{L}_{\mathrm{gaze}}$$
