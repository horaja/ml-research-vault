# Contrastive Alignment for Task-Conditioned Patch Selection

> Deep dive into a TRIPS-inspired approach to Module 1: project vision patches and language embeddings into a shared space, score patches by cross-modal similarity, select top-$k$. Optionally pre-train with DAA gaze data via an energy-based contrastive objective, then fine-tune end-to-end on BEHAVIOR-1K.

---

## 1. Motivation

The simplest possible Module 1 that provides genuine cross-modal grounding. The current system scores patches by overlap with line drawing edges—a static, task-agnostic heuristic. This approach replaces it with a learned scoring function that additionally conditions on the language instruction, while preserving the same downstream interface: a scalar score per patch → top-$k$ selection.

The core insight from TRIPS (Fu et al., 2023): text-guided patch selection can be implemented as a lightweight layer *inside* the visual backbone that dynamically computes text-dependent attention to identify important patches and fuse inattentive ones, without introducing extra parameters to the ViT. The mechanism is simple enough to prototype in 1–2 days given an existing codebase.

### Why This Over Architecture C

Architecture C (variational spatial prior) gives you principled uncertainty, a standalone language-only prior, and elegant integration with iterative refinement. But it introduces β-tuning, posterior collapse risks, and KL balancing complexity. Contrastive alignment is the **minimal viable Module 1**: if it fails to improve over the line-drawing baseline, the problem isn't the formulation—it's that language doesn't help for this task. If it succeeds, you have a working system and can decide whether the variational layer is worth the added complexity.

---

## 2. Core Mechanism

### 2.1 Overview

```
Input:  N patch embeddings {v₁, ..., v_N}, language embedding l
Output: Top-k patch indices, ordered by cross-modal relevance score
```

Three steps:

1. **Project** both modalities into a shared $d$-dimensional space.
2. **Score** each patch by cosine similarity to the language embedding.
3. **Select** the top-$k$ patches by score.

### 2.2 Projection into Shared Space

```
z_v_i = normalize(W_v · v_i + b_v)      # for each patch i = 1..N
z_l   = normalize(W_l · l   + b_l)      # single language vector
```

Where:
- $W_v \in \mathbb{R}^{d \times d_v}$ projects patch embeddings (dim $d_v$) to shared space (dim $d$)
- $W_l \in \mathbb{R}^{d \times d_l}$ projects language embedding (dim $d_l$) to shared space (dim $d$)
- `normalize` = L2 normalization (project onto unit hypersphere)

**Total new parameters:** $d \times d_v + d \times d_l + 2d$ (biases). For $d = 128$, $d_v = 384$, $d_l = 384$: approximately 98K parameters. Negligible.

### 2.3 Scoring

$$s_i = \frac{z_{v_i}^\top z_l}{\tau}$$

where $\tau > 0$ is a learnable or fixed temperature. The cosine similarity in the shared space measures "does this patch's content relate to what the instruction describes?"

The score distribution over patches:

$$\alpha_i = \frac{\exp(s_i)}{\sum_{j=1}^{N} \exp(s_j)}$$

### 2.4 Selection

**During inference (hard selection):**

$$\text{selected} = \text{top-}k(\{s_1, \ldots, s_N\})$$

Discard unselected patches. Downstream ViT processes only $k$ tokens.

**During training (differentiable selection):**

Option A — **Soft weighting:** Weight all patch embeddings by $\alpha_i$ before passing to downstream. Fully differentiable, but no efficiency gain during training.

Option B — **Straight-through Gumbel top-$k$:** Sample $k$ patches using Gumbel-softmax in the forward pass (hard selection), but use the continuous relaxation for gradients in the backward pass.

Option C — **Perturbed top-$k$ (Berthet et al., 2020):** Add noise to scores, take hard top-$k$, estimate gradients via perturbation. More principled than straight-through but slightly more complex.

**Recommendation:** Start with Option A (soft weighting) for simplicity. If the soft-hard gap at inference time is a problem, switch to Option B.

---

## 3. What Are the Patch Embeddings?

The input $v_i$ to the projection layer. This is a critical design choice because it determines what information the scoring function can use.

### 3.1 Option Landscape

| Option | Source | $d_v$ | Pros | Cons |
|---|---|---|---|---|
| **(a)** Line drawing features | Small CNN on line drawing patch | ~128 | Independent of downstream ViT; no circular dependency; directly extends current system | Limited semantic content; only captures edge/contour structure |
| **(b)** ViT patch embedding | First linear layer of the downstream ViT ($\text{pixels} \to \text{tokens}$) | 768 | Shared representation; minimal overhead | Couples Module 1 to backbone; mild circular dependency |
| **(c)** Frozen DINOv2 features | DINOv2 ViT-S/14 on original image patches | 384 | Rich semantic features; known to capture object parts and boundaries well | Additional forward pass through frozen encoder at inference |
| **(d)** Hybrid: line drawing + frozen features | Concatenation of (a) and (c) | ~512 | Best of both: biological structure from line drawings + semantic richness from DINOv2 | Most expensive; largest projection matrix |

### 3.2 Recommendation

Start with **(a)** (line drawing features alone) to validate that language conditioning adds value beyond the existing task-agnostic scoring. This is the most direct comparison: same visual input, but now with language modulation.

If language adds measurable value with (a), upgrade to **(d)** to see if richer features help further. The line drawing component preserves your biological motivation; the DINOv2 component adds the semantic content that language needs to ground against (e.g., color, texture, object identity—things line drawings don't capture).

### 3.3 Incorporating Line Drawings as a Feature

Currently the system scores patches by line drawing edge overlap. Rather than replacing this, **augment** it:

```
# Existing features (task-agnostic)
edge_score_i = line_drawing_overlap(patch_i)         # scalar
edge_map_i   = line_drawing_crop(patch_i)            # local edge image

# New features
cnn_features_i = small_cnn(edge_map_i)               # learned edge features, dim ~64
v_i = concat(cnn_features_i, [edge_score_i])          # dim ~65

# With language conditioning
z_v_i = normalize(W_v · v_i)
z_l   = normalize(W_l · l)
s_i   = z_v_i · z_l / τ
```

The existing edge score becomes one feature among many. If language conditioning doesn't help, the model can learn to rely primarily on the edge score, recovering the current system. If it does help, the CNN features + language interaction captures what the scalar overlap misses.

---

## 4. Language Embedding Choice

The embedding $l$ that the scoring function conditions on.

### 4.1 Options

| Encoder | Dim | Pre-training | Notes |
|---|---|---|---|
| **DeCLUTR** (as in DAA) | 384 | Unsupervised paraphrase | Already in the DAA pipeline; consistent with Kim et al. |
| **paraphrase-MiniLM** (as in HULC) | 384 | Paraphrase corpus | Lightweight; used in HULC/HULC++ |
| **CLIP ViT-B/16 text encoder** | 512 | Image-text contrastive | Already aligned with visual features; strongest option if patch features come from CLIP-compatible vision encoder |
| **SigLIP text encoder** | 768 | Sigmoid contrastive | Newer CLIP variant; slightly better fine-grained grounding |

### 4.2 Recommendation

If patch embeddings are from a frozen CLIP/SigLIP vision encoder, use the matching text encoder. The shared pre-trained space means $W_v$ and $W_l$ can be initialized near identity—the scoring function starts with a strong prior and only needs fine-tuning for manipulation-specific relevance.

If patch embeddings are from line drawings or a custom CNN (no pre-trained vision-language alignment), use **paraphrase-MiniLM** or **DeCLUTR** for consistency with the existing pipeline. The projection matrices $W_v, W_l$ will need to learn the cross-modal alignment from scratch, which requires more training signal.

**Always freeze the text encoder.** Your dataset is too small to fine-tune a language model. The projection matrix $W_l$ is the adapter.

---

## 5. Training: Two-Stage Approach

The key recommendation: **pre-train the scoring function with contrastive gaze supervision on DAA data, then fine-tune end-to-end on BEHAVIOR-1K with action prediction loss.** This combines the strengths of direct spatial supervision (fast convergence) with domain adaptation (BEHAVIOR-1K alignment).

### 5.1 Stage 1: Contrastive Pre-training on DAA Gaze Data

The DAA dataset provides (image, language instruction, gaze coordinates) triples. Use these to train the scoring function to assign high similarity to patches that humans fixated on.

**Positive patches:** Patches whose spatial extent overlaps with the gaze coordinate $(g_x, g_y)$. Use a Gaussian kernel for soft positives—patches near gaze get higher weight.

**Negative patches:** All other patches in the same image, plus patches from other images in the batch (cross-image negatives).

**Loss function (InfoNCE):**

$$\mathcal{L}_{\text{contrastive}} = -\log \frac{\exp(s^+ / \tau)}{\sum_{j=1}^{N} \exp(s_j / \tau)}$$

where $s^+ = z_{v^+}^\top z_l / \tau$ is the score of a positive (gazed-at) patch, and the denominator sums over all patches (positive + negative).

**With soft positives (Gaussian-weighted):**

```python
# Compute gaze proximity weight for each patch
w_i = exp(-||patch_center_i - (gx, gy)||² / (2σ²))
w   = w / w.sum()                                    # normalize

# Weighted contrastive loss
L = -Σ_i w_i · log(exp(s_i/τ) / Σ_j exp(s_j/τ))
```

This is softer than hard InfoNCE—patches near the gaze contribute proportionally to their proximity, rather than a binary positive/negative split.

**Batch construction:** Each batch contains multiple (image, instruction, gaze) triples from DAA. Cross-image negatives come for free: patches from other images in the batch serve as hard negatives for each query instruction.

**Training details:**
- Freeze text encoder entirely
- Train $W_v$, $W_l$, and patch CNN (if used)
- Learning rate: 1e-4 with cosine decay
- Batch size: 32–64 (larger batches give more informative negatives)
- Temperature $\tau$: initialize at 0.07 (CLIP default), optionally make learnable
- Epochs: 20–50 on DAA data (dataset is small; watch for overfitting)

### 5.2 Stage 2: End-to-End Fine-tuning on BEHAVIOR-1K

After pre-training, the scoring function already assigns high similarity to task-relevant patches for instructions it has seen. Now fine-tune the entire pipeline (Module 1 + downstream ViT + policy) on BEHAVIOR-1K using the action prediction loss.

```python
for each batch (x, l, a) from BEHAVIOR-1K:
    
    # Score patches using pre-trained Module 1
    v_i   = patch_encoder(patches(x))
    z_v_i = normalize(W_v · v_i)
    z_l   = normalize(W_l · l)
    s_i   = z_v_i · z_l / τ
    α     = softmax(s / τ)                           # attention weights
    
    # Select patches (soft during training)
    selected = Σ_i α_i · v_i                         # weighted combination
    # Or: selected = top_k_gumbel(s, k)              # hard differentiable
    
    # Run downstream pipeline
    image_embedding = vit(selected)                   # via DINOv2 or similar
    â = policy(image_embedding, l)
    
    # Action prediction loss
    L = action_loss(â, a)
    
    # Backprop through everything including W_v, W_l, patch_encoder
    optimizer.step()
```

**What fine-tuning adapts:** The pre-trained scoring function knows "where humans look given an instruction" from DAA. Fine-tuning on BEHAVIOR-1K adapts it to "where should the model look to predict *actions* for these specific tasks." These may differ—a human might glance at an object to identify it, but the policy might need patch information about the grip surface or the obstacle geometry.

**Learning rate schedule:** Lower learning rate for the pre-trained components ($W_v$, $W_l$, patch encoder) than for the randomly-initialized downstream components (policy, etc.). Ratio: 10x lower for pre-trained parts.

### 5.3 Optional: Joint Training (No Pre-training)

If DAA gaze data is unavailable or you want to skip Stage 1:

Train the scoring function jointly with the downstream pipeline, using only the action prediction loss. The gradient signal for Module 1 comes entirely from the action loss flowing back through the selected patches.

**This is weaker.** The action loss is a distant, noisy signal for "which patches matter"—the gradient must flow through the ViT, the policy, and the selection mechanism before reaching $W_v$ and $W_l$. But it works: TRIPS demonstrated this approach on VLP tasks without any explicit spatial supervision.

**Warm-start from CLIP:** If using CLIP-compatible patch features, initialize $W_v = I$ and $W_l = I$ (identity matrices, possibly with appropriate dimensionality adjustment). The scoring function then starts with CLIP's pre-trained cross-modal alignment—"red cup" already scores high against patches containing red cups. Fine-tuning only needs to adjust for manipulation-specific relevance.

---

## 6. Connection to the Energy-Based Formulation

The contrastive alignment approach and the energy-based approach are two views of the same mechanism.

### 6.1 Equivalence

Define the energy function:

$$E_\theta(v_i, l) = -\frac{z_{v_i}^\top z_l}{\tau} = -\frac{(W_v v_i)^\top (W_l l)}{\|W_v v_i\| \|W_l l\| \cdot \tau}$$

Then:

$$\alpha_i = \mathrm{softmax}(-E_\theta(v_i, l)) = \frac{\exp(z_{v_i}^\top z_l / \tau)}{\sum_j \exp(z_{v_j}^\top z_l / \tau)}$$

The contrastive loss (InfoNCE) is equivalent to training this energy function to assign low energy (high similarity) to positive (patch, language) pairs and high energy (low similarity) to negatives.

### 6.2 Why Frame It as Contrastive Alignment Rather Than Energy-Based

1. **Implementation clarity.** "Project to shared space, compute cosine similarity" is easier to implement correctly than "define an energy function, train with contrastive loss." They're the same math, but the shared-space framing maps more directly to code.

2. **Pre-training leverage.** CLIP, SigLIP, and other contrastive models provide pre-trained shared spaces. You can warm-start from them. There's no equivalent "pre-trained energy function" to initialize from.

3. **Established tooling.** The contrastive learning literature has mature implementations of InfoNCE, hard negative mining, temperature scheduling, etc.

### 6.3 Richer Energy Functions

If cosine similarity is too weak (can't capture complex patch-language relationships), you can upgrade the scoring function while keeping the contrastive training:

**Bilinear scoring:**
$$s_i = v_i^\top M l$$

where $M \in \mathbb{R}^{d_v \times d_l}$ is a learned interaction matrix. More expressive than two separate projections + cosine. Parameters: $d_v \times d_l$.

**MLP scoring:**
$$s_i = \text{MLP}(\text{concat}(v_i,\; l,\; v_i \odot l))$$

Most expressive. The Hadamard product $v_i \odot l$ captures multiplicative interactions. Parameters: depends on MLP width, but ~50K–200K is sufficient.

**Recommendation:** Start with cosine similarity (simplest). If ablations show that language conditioning adds negligible value over the line-drawing baseline, upgrade to MLP scoring before concluding that language doesn't help—the problem might be that cosine similarity is too weak a coupling, not that language is uninformative.

---

## 7. Relationship to TRIPS

TRIPS (Fu et al., 2023) is the closest prior work to this approach. Key similarities and differences:

### 7.1 What TRIPS Does

TRIPS inserts a text-guided patch selection layer inside the ViT backbone. At intermediate layers, it:

1. Computes attention between the text `[CLS]` token and all visual patch tokens.
2. Uses these attention scores to rank patches by text-relevance.
3. Keeps the top-$k$ patches (attentive tokens) and fuses the rest (inattentive tokens) into a single summary token via weighted averaging.
4. The ViT continues processing with fewer tokens.

This is progressive—selection happens at multiple ViT layers, reducing tokens gradually.

### 7.2 Key Differences from Your Setup

| Aspect | TRIPS | Your Module 1 |
|---|---|---|
| **Where selection happens** | Inside the ViT, at intermediate layers | Before the ViT, at the input |
| **Scoring signal** | Cross-attention between text CLS and ViT intermediate features | Cross-modal similarity in a learned shared space |
| **What drives training** | VLP objectives (ITC, ITM, MLM) | Action prediction loss (+ optional gaze contrastive loss) |
| **Fusion of unselected patches** | Weighted average into a summary token (information preserved) | Discarded (information lost) |
| **Progressive vs. one-shot** | Progressive (multiple selection stages through ViT depth) | One-shot (select once, then process) |

### 7.3 What to Borrow from TRIPS

**The summary token idea.** Rather than discarding unselected patches entirely, fuse them into a single "background" token via weighted averaging. This preserves some global context at minimal cost (one extra token). The downstream ViT then processes $k + 1$ tokens instead of $k$.

```python
# After scoring and selecting top-k
selected_patches = patches[top_k_indices]
unselected_patches = patches[~top_k_indices]
α_unselected = softmax(scores[~top_k_indices])
summary_token = Σ α_unselected_j · unselected_patches_j

# Concatenate and pass to ViT
input_tokens = concat(selected_patches, summary_token)
```

This is a cheap safety net: if the scoring function makes a mistake and discards an important patch, the summary token partially preserves its information.

**Progressive selection.** Instead of selecting all $k$ patches at once before the ViT, select $k_1$ patches before the ViT, then after $L_1$ ViT layers, re-score and potentially swap patches using the richer intermediate representations. This mirrors the iterative refinement in your architecture diagram, but implemented inside the ViT rather than as an external loop.

---

## 8. Evaluation Strategy

### 8.1 Does Language Actually Help?

The first and most important ablation. Compare:

| Condition | Scoring function | Expected outcome |
|---|---|---|
| **Baseline** | Line drawing edge overlap (no language) | Current 75.8% on ImageNet-10 at 40% patches |
| **Language-conditioned** | Cosine similarity in shared space (with language) | Should improve if instructions disambiguate attention |
| **Language ablation** | Same architecture, but replace language with a zero vector | Isolates the effect of language from the effect of learned (vs. handcrafted) visual scoring |

If the language-conditioned model doesn't beat the language-ablation model, language is not providing useful spatial information for this task. This is a critical diagnostic before investing in Architecture C.

### 8.2 Attention Map Quality

Compute correlation between the model's patch scores and human gaze maps from DAA (Option B from Overview.md).

**Metrics:**
- **Spearman rank correlation** between patch scores and gaze density per patch
- **Normalized Scanpath Saliency (NSS):** the model's score at fixated locations, normalized
- **AUC-Judd:** area under ROC curve treating gaze points as positives

Compare these for the line-drawing baseline vs. the contrastive model. If the contrastive model's attention maps are more correlated with human gaze, it's learning a more human-like prior.

### 8.3 Downstream Task Performance

The ultimate evaluation: action prediction quality on BEHAVIOR-1K manipulation tasks.

**Metrics:**
- Task success rate at various token budgets ($k = 0.2N$, $0.4N$, $0.6N$)
- GFLOPs per action prediction
- Sample efficiency: demonstrations needed for target performance

Plot the success-rate-vs-token-budget curve. A better prior shifts this curve left (same success at fewer tokens).

---

## 9. Failure Modes

### 9.1 Language Adds No Value

**Symptom:** Language-conditioned model performs identically to language-ablation model.

**Diagnosis:** Either the language embeddings don't carry spatial information for these instructions, or the projection matrices can't learn the right mapping from limited data.

**Mitigations:**
- Check language encoder quality: embed several instructions and verify they're distinguishable (cluster analysis)
- Upgrade from cosine similarity to MLP scoring (richer cross-modal interaction)
- Pre-train with DAA gaze data (direct supervision for language-attention mapping)
- Try richer language encoders (CLIP text encoder instead of DeCLUTR)

### 9.2 Scoring Collapse

**Symptom:** All patches receive near-identical scores regardless of instruction. Selection is effectively random.

**Diagnosis:** The projection matrices have collapsed—either $W_v$ projects all patches to similar vectors, or $W_l$ ignores the instruction.

**Mitigations:**
- Temperature tuning: $\tau$ too high makes all scores similar after softmax
- Gradient monitoring: check that $W_v$ and $W_l$ are both receiving meaningful gradients
- Pre-training on DAA (provides direct, strong gradient signal to both projections)

### 9.3 Distribution Shift (DAA → BEHAVIOR-1K)

**Symptom:** Model performs well on DAA scenes but degrades on BEHAVIOR-1K.

**Diagnosis:** The scoring function has overfit to DAA's visual distribution (specific objects, camera angles, lighting).

**Mitigations:**
- Stage 2 fine-tuning (§5.2) is specifically designed to handle this
- Regularize during pre-training: dropout on patch features, data augmentation
- Use frozen DINOv2 features (option c in §3.1)—these are domain-general

### 9.4 Top-$k$ Sensitivity

**Symptom:** Performance varies dramatically with $k$. Too few patches = critical information lost; too many = no efficiency gain.

**Diagnosis:** The scoring function doesn't separate relevant from irrelevant patches cleanly—the score distribution has low dynamic range.

**Mitigations:**
- Inspect the score distribution: if it's nearly uniform, the model hasn't learned meaningful scoring
- Use the TRIPS summary token (§7.3) as a safety net for discarded patches
- Adaptive $k$: instead of fixed top-$k$, select all patches with $\alpha_i > \text{threshold}$. The number of selected patches varies per example.

---

## 10. Minimal Prototype: Integration with Existing Codebase

Assuming the current system has: a line drawing generator, a patch scorer (edge overlap), a top-$k$ selector, and a downstream ViT + policy.

### 10.1 Changes Required

**New components (implement):**
- `PatchProjector`: Linear layer $W_v$ mapping patch features to shared space
- `LanguageProjector`: Linear layer $W_l$ mapping language embeddings to shared space
- `CrossModalScorer`: Cosine similarity + temperature + softmax

**Modified components:**
- `PatchScorer`: Replace `edge_overlap(patch)` with `cross_modal_score(patch, instruction)`
- Training loop: Add contrastive pre-training stage (optional), add gradient flow from action loss back to projectors

**Unchanged components:**
- Line drawing generator (still produces visual features; now fed into `PatchProjector`)
- Top-$k$ selector (same interface: takes scores, returns indices)
- Downstream ViT + policy (receives selected patches as before)

### 10.2 The Forward Pass Change

**Before:**
```python
score_i = line_drawing_overlap(patch_i)
selected = top_k(scores, k)
output = policy(vit(selected_patches), instruction)
```

**After:**
```python
v_i     = patch_encoder(patch_i, line_drawing_i)    # embed patch + LD features
z_v_i   = normalize(W_v @ v_i)                       # project to shared space
z_l     = normalize(W_l @ text_encoder(instruction)) # project language
score_i = (z_v_i * z_l).sum() / τ                    # cosine similarity
selected = top_k(scores, k)
output   = policy(vit(selected_patches), instruction)
```

Same downstream interface. Same selection mechanism. The only change is how scores are computed.

---

## 11. Relation to Architecture C

Contrastive alignment is **Stage 1** of Architecture C. Specifically:

| Component | Contrastive Alignment | Architecture C |
|---|---|---|
| Posterior scoring | ✅ Cross-modal similarity $(v_i, l) \to s_i$ | ✅ Same, but outputs distributional parameters $(\mu, \sigma)$ |
| Prior network | ❌ None | ✅ $p_\theta(z \mid l)$ — language-only spatial prediction |
| KL regularization | ❌ None | ✅ Posterior must match prior |
| Spatial uncertainty | ❌ None (scalar score only) | ✅ $\sigma_{\mathrm{post}}$ per patch |
| Iterative refinement | Via external Module 3 | Native: prior → Pass 1, posterior → Pass 2, $\sigma$ → Pass 3 |
| Training complexity | Low (one loss term + optional contrastive pre-training) | High (ELBO, β-tuning, KL balancing, collapse monitoring) |

### Upgrade Path

If contrastive alignment works and you want to add the variational layer:

1. Take the trained $W_v$, $W_l$, and patch encoder from this approach.
2. Add prior network $p_\theta(z \mid l)$ and posterior variance head $\sigma_{\mathrm{post}}$.
3. Add KL loss with low β.
4. The contrastive pre-training initializes the posterior's scoring; the KL term shapes the prior.

This is the smoothest path from prototype to full Architecture C. Each stage builds on the previous one. Nothing is thrown away.

---

## 12. Implementation Plan

| Day | Task | Validates |
|---|---|---|
| 1 | Implement `PatchProjector`, `LanguageProjector`, `CrossModalScorer` | Code compiles, shapes match |
| 2 | Integrate into existing pipeline; replace edge overlap scorer | Forward pass runs end-to-end |
| 3 | Train with action prediction loss only (no pre-training) | Gradient flows to projectors; scores differentiate |
| 4 | Run ablation: language-conditioned vs. zero-language vs. edge-overlap baseline | **Does language help?** (critical diagnostic) |
| 5 | (If language helps) Implement contrastive pre-training on DAA | Attention maps correlate with gaze |
| 6 | Two-stage training: DAA pre-train → BEHAVIOR-1K fine-tune | Full pipeline evaluation |
| 7 | TRIPS summary token + adaptive $k$ | Robustness to $k$ selection |

---

## 13. Key Equations Summary

**Projection:**
$$z_{v_i} = \frac{W_v v_i + b_v}{\|W_v v_i + b_v\|_2}, \quad z_l = \frac{W_l l + b_l}{\|W_l l + b_l\|_2}$$

**Scoring:**
$$s_i = \frac{z_{v_i}^\top z_l}{\tau}$$

**Attention weights:**
$$\alpha_i = \frac{\exp(s_i)}{\sum_{j=1}^{N} \exp(s_j)}$$

**Contrastive pre-training loss (soft InfoNCE with gaze):**
$$\mathcal{L}_{\text{contrastive}} = -\sum_{i=1}^{N} w_i \cdot \log \frac{\exp(s_i / \tau)}{\sum_{j=1}^{N} \exp(s_j / \tau)}$$

where $w_i = \frac{\exp\big(-\|c_i - g\|^2 / 2\sigma^2\big)}{\sum_j \exp\big(-\|c_j - g\|^2 / 2\sigma^2\big)}$ is the Gaussian gaze proximity weight for patch $i$ with center $c_i$ and gaze point $g$.

**End-to-end fine-tuning loss:**
$$\mathcal{L}_{\text{total}} = \mathcal{L}_{\text{action}}(\hat{a}, a)$$

where $\hat{a} = \text{policy}(\text{ViT}(\text{select}(x, \alpha)), l)$ and gradients flow through $\alpha$ back to $W_v, W_l$.

**Optional joint loss (with DAA data available during fine-tuning):**
$$\mathcal{L}_{\text{total}} = \mathcal{L}_{\text{action}} + \lambda \cdot \mathcal{L}_{\text{contrastive}}$$
