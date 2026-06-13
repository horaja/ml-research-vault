---
type: experiment
status: planned
project: surf
---

# variational spatial prior

## hypothesis
Treating the patch attention map as a latent variable with a language-only prior $p_\theta(z|l)$ and an image+language posterior $q_\phi(z|x,l)$, trained via ELBO, yields (a) a usable language-only first-pass selector, (b) per-patch uncertainty $\sigma_{\text{post}}$ for iterative refinement, and (c) stronger language-conditioning than the contrastive scorer in [[experiments/contrastive alignment]].

## setup
- Posterior: cross-modal MLP scorer over `concat(v_i, l, v_i ⊙ l)` outputting `(μ_post, σ_post)` per patch.
- Prior: MLP from frozen text encoder → `(μ_prior, σ_prior)` per patch (upgrade path: 2D GMM rendered onto patch grid).
- Patch features: line-drawing CNN by default (avoids circular dependency); optional frozen DINOv2 upgrade.
- Language: frozen text encoder (DeCLUTR or CLIP-text).
- Selection: reparameterize `z = μ_post + σ_post ⊙ ε`; soft `softmax(z/τ)` train, top-k inference.
- Loss: `L_recon + β · KL(q_φ ‖ p_θ)` with KL-free warmup, linear β anneal, free-bits, asymmetric KL balancing (prior 0.8 / posterior 0.2).
- Optional auxiliary: DAA gaze KL on prior and posterior; gripper-close KL on posterior for BEHAVIOR.
- Iterative use: Pass 1 = prior only; Pass 2 = posterior; Pass 3 = add patches from high-$\sigma_{\text{post}}$ regions.
- Fine-tune end-to-end on BEHAVIOR.

## baselines
- [[experiments/contrastive alignment]] (point-estimate scorer, no prior, no σ).
- Same posterior, β=0 (no KL) — isolates the KL contribution.
- Prior-only at test time (no Pass 2) — isolates language-only spatial signal.
- Line prior only; language-zeroed; random; center-bias (carried from contrastive alignment).

## metric
- Gaze alignment ([[eval/gaze]]).
- Task-relevant reconstruction ([[eval/reconstruction]]).
- Task success and GFLOPs/action on BEHAVIOR, broken down by pass (1, 1+2, 1+2+3).
- Calibration of $\sigma_{\text{post}}$: does high σ predict where Pass 3 helps?

## result
TBD.

## interpretation
TBD.

## failure analysis
Anticipated failure modes from archived design:
- Posterior collapse (KL → 0 early, reconstruction plateau).
- Prior underfitting (KL stays high, prior maps uniform).
- Attention mode collapse (always same patches).
- Gaze-language decorrelation (DAA gaze invariant to instruction phrasing).
- Circular dependency if posterior input leaks selected-patch features.

## baseline that could kill the claim
Same posterior trained with β=0 (no prior, no KL) matching this method on task success and gaze alignment — would imply the variational machinery adds nothing over a richer learned scorer, and the contrastive alignment upgrade path (MLP scorer + Hadamard) is the right stopping point.

## next action
- Decide: independent-Gaussian prior vs 2D GMM prior.
- Decide: whether DAA gaze loss is on by default (carries DAA→BEHAVIOR shift caveat).
- Lock β schedule and free-bits threshold.
- Confirm posterior patch input source (line-drawing CNN vs frozen DINOv2) — must satisfy no-circular-dependency rule from [[concepts/selector]].

## links
- [[experiments/contrastive alignment]]
- [[concepts/selector]]
- [[concepts/variational prior]]
- [[claims/iterative selection]]
- [[synthesis/prior vs learned]]
- [[eval/gaze]]
- [[eval/reconstruction]]
- [[behavior env stanford]]
