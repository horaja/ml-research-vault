> This metric answers: **"Given the patches my prior selected, how much task-relevant information was captured?"**

---

## The Metric (Formal Definition)

$$Q(\text{Task}, \text{Prior}) = -D(W \odot I, \, W \odot I^R)$$

Where:
- $I$ = original RGB frame (224×224) from the robot camera
- $I^R = \text{MAE}(P_{\text{selected}})$ = reconstruction from only the selected patches
- $W$ = binary mask over task-relevant pixels (from ground-truth segmentation + BDDL task objects)
- $D$ = dissimilarity function (SSIM primary, LPIPS secondary, MSE tertiary)
- $P_{\text{selected}}$ = the $k$ patches chosen by the prior being evaluated

**Normalized version** (removes MAE capacity confound):
$$\hat{Q} = \frac{Q(\text{Prior})}{Q(\text{All Patches})}$$

---

## High-Level Action Items

### Phase 0: Environment Setup
- [ ] Install OmniGibson on NI cluster (Isaac Sim dependency, GPU requirements)
- [ ] Verify a single BehaviorTask loads and renders RGB + semantic segmentation
- [ ] Confirm VisionSensor resolution is set to 224×224
	- [ ] Verify segmentation label format: `info["robot0"]["robot0:eyes:Camera:0"]["seg_semantic"]` maps pixel values to synset names
- [ ] Run `get_obs()` and save one frame's RGB + seg_semantic + seg_info to disk as a sanity check

### Phase 1: W-Mask Construction Module
**Input:** BDDL task definition + semantic segmentation map + segmentation label info dict
**Output:** Binary mask $W$ of shape (224, 224)

Steps:
- [ ] Parse BDDL `:objects` block to extract the set of task-relevant synsets (e.g., `candle.n.01`, `wicker_basket.n.01`)
- [ ] From `seg_info`, build a lookup: pixel_value → synset_name
- [ ] For each pixel in `seg_semantic`, set $W[x,y] = 1$ if its synset is in the task-relevant set, else 0
- [ ] Downsample $W$ to patch grid (14×14 for ViT-B/16 on 224×224): a patch is task-relevant if ≥ 1 pixel in the patch belongs to a task-relevant object (threshold = any nonzero overlap; can be tuned later)
- [ ] Store both pixel-level $W$ (for $D$ computation) and patch-level $W_{\text{patch}}$ (for coverage metric)

**Key design decision:** Treat all BDDL-listed objects uniformly in $W$ (do not weight by proximity or subtask relevance). This is the simplest defensible choice. Weighting is a future extension.

### Phase 2: Coverage Metric (Sanity Check, No MAE Needed)
**Input:** Patch selection mask (14×14 binary), $W_{\text{patch}}$ (14×14 float)
**Output:** Scalar coverage score

$$Q_{\text{coverage}} = \frac{\sum_{p \in \text{selected}} W_{\text{patch}}[p]}{\sum_{\text{all } p} W_{\text{patch}}[p]}$$

This is the fraction of task-relevant patch-area captured by the selection. Implement this first because:
- Zero external dependencies
- Immediate sanity check: random selection should give coverage ≈ k/196; a good prior should be much higher
- If coverage doesn't discriminate between priors, something is wrong with $W$

### Phase 3: MAE Reconstruction Pipeline
**Input:** RGB frame (224×224), patch selection mask
**Output:** Reconstructed image $I^R$ (224×224)

Steps:
- [ ] Load pretrained MAE-ViT-Large (facebook/mae-vit-large-patch16-224 from HuggingFace)
- [ ] Implement the selective reconstruction: given an image and a set of selected patch indices, mask out unselected patches, run through MAE decoder, output reconstructed image
- [ ] Test on 5 BEHAVIOR frames: verify reconstruction looks plausible with 100% patches, visibly degraded with 40% random patches
- [ ] If reconstruction is uniformly terrible (domain gap), consider finetuning MAE on ~2k BEHAVIOR frames for ~10 epochs (fallback only)

**Critical note:** The MAE's native masking during pretraining used random masks. Your evaluation uses structured masks (prior-selected patches). The MAE may behave differently with structured vs. random masking patterns. Test this explicitly.

### Phase 4: Dissimilarity Functions $D$
Implement three dissimilarity functions operating on masked image regions:

**SSIM (primary):**
- Compute SSIM between $W \odot I$ and $W \odot I^R$ using `pytorch_msssim` or `skimage.metrics.structural_similarity`
- Only compute over the bounding box of $W$ (not the full image) to avoid inflating SSIM with matched-zero regions outside the mask
- Window size: 7×7 or 11×11 (standard)

**LPIPS (secondary):**
- Use `lpips` package with VGG backbone
- Apply $W$ as a spatial mask to the feature maps, not to the input images (masking input images would create artificial edges the network would detect)
- Alternative: crop to bounding box of $W$ and compute LPIPS on the crop

**MSE (tertiary, appendix only):**
- $D_{\text{MSE}} = \frac{1}{|W|} \sum_{(x,y) \in W} (I[x,y] - I^R[x,y])^2$

### Phase 5: Baseline Priors
Implement these patch selection strategies for comparison:

1. **Random:** Select $k$ patches uniformly at random. Run 10+ seeds, report mean ± std.
2. **Center bias:** Select $k$ patches closest to image center (Euclidean distance from patch center to image center). This is the most common confound in attention models.
3. **Edge density (Canny):** Run Canny edge detector on RGB, count edge pixels per patch, select top-$k$. This is the naive structural baseline your line-drawing prior must beat.
4. **Line drawing overlap:** Run informative-drawings generator, score patches by overlap with drawn lines, select top-$k$. This is your current Module 1 prior (non-task-specific version).
5. **Oracle (upper bound):** Greedy search — iteratively add the patch that most improves $\hat{Q}$. Computationally expensive (196 × k forward passes per frame). Run on a small subset of frames only.

### Phase 6: Evaluation Loop
For each task, for each prior, for each patch budget $k$:
- [ ] Collect $N$ frames (uniform subsampling, every $n$-th frame from an episode)
- [ ] For each frame: construct $W$, run prior → get patch selection, run MAE → get $I^R$, compute $D$, compute normalized $\hat{Q}$
- [ ] Aggregate: mean $\hat{Q}$ across frames, report with 95% CI
- [ ] Plot: $\hat{Q}$ vs. $k$ curves for each prior (the main result figure)

### Phase 7: Task Selection for Evaluation
Evaluate on these 6 BEHAVIOR-1K tasks:

| Task                               | Type                              | Why                                                          |
| ---------------------------------- | --------------------------------- | ------------------------------------------------------------ |
| turning_on_radio                   | Single-object, articulated        | Small task-relevant region, tests localization precision     |
| sorting_vegetables                 | Multi-object pick-and-place       | Distributed task objects, tests multi-region attention       |
| putting_dishes_away_after_cleaning | Multi-step, shifting relevance    | Task-relevant region changes across episode phases           |
| chop_an_onion                      | Fine manipulation + tool use      | Tiny contact region, high spatial precision needed           |
| storing_food                       | Medium complexity, clear objects  | Calibration task — if metric fails here, it fails everywhere |
| assembling_gift_baskets            | Many objects (16+), complex goals | Stress test for scaling                                      |

---

## Things to Keep in Mind

### Patch Grid Alignment
- ViT-B/16 on 224×224 → 14×14 = 196 patches, each 16×16 pixels
- All patch selections, coverage computations, and attention maps operate on this 14×14 grid
- $W$ must be downsampled to this grid for coverage, but $D$ is computed at full 224×224 resolution on the masked images

### The Normalization Is Essential
Without normalizing by $Q(\text{All Patches})$, you're measuring a joint property of the prior AND the MAE. The normalization isolates the prior's contribution. Always report $\hat{Q}$, not raw $Q$.

### Patch Budgets to Sweep
Report results for $k \in \{20, 40, 60, 80, 100, 120\}$ patches (roughly 10%–60% of 196 total). Your proposal targets "comparable task success with 40–60% fewer tokens," so the range around 80–120 patches (40–60% of 196) is where your prior needs to shine.

### Frame Sampling
Uniform subsampling: every 10th frame from each episode is sufficient for the evaluation metric. Don't overthink this — it's a parameter you can tune later.

### Reproducibility
Set random seeds for all stochastic baselines. Save all intermediate outputs (W masks, patch selections, reconstructions) to disk for debugging. Log everything.

---

## Future Extensions (Not for Now)

- **Phase-aware evaluation:** Separately report metrics during approach, contact, and manipulation phases (detected from proprioception signals like gripper force/position)
- **Temporal aggregation:** Instead of per-frame metrics, evaluate whether the prior's selections are temporally coherent (penalize jittery attention maps)
- **Object-weighted $W$:** Weight task-relevant objects by proximity to end-effector or by role in current subtask (requires parsing BDDL goal predicates at each timestep)
- **VLA encoder distance (Option 3 from brainstorm):** Replace MAE reconstruction with representation distance in the VLA's vision encoder — this becomes feasible once you integrate OpenVLA-OFT via the BEHAVIOR baselines
- **Cross-domain evaluation:** Run the same metric on DAA dataset frames (real images) to test whether the prior generalizes beyond rendered scenes
- **Learned $D$ function:** Train a task-specific dissimilarity function that weights reconstruction errors by action-relevance (e.g., errors near contact points matter more)

---

## Dependencies Summary

| Component | Source | Required For |
|-----------|--------|-------------|
| OmniGibson | `pip install omnigibson` + Isaac Sim | Environment, rendering, segmentation |
| BDDL | `pip install bddl` (bundled with OmniGibson) | Task definitions, object lists |
| MAE-ViT-Large | `facebook/vit-mae-large` from HuggingFace | Reconstruction |
| pytorch-msssim | `pip install pytorch-msssim` | SSIM computation |
| lpips | `pip install lpips` | LPIPS computation |
| informative-drawings | github.com/carolineec/informative-drawings | Line drawing baseline |
| OpenCV | `pip install opencv-python` | Canny edge baseline |

---

## Success Criteria

The metric is working correctly when:
1. Coverage metric produces: random ≈ $k$/196, oracle ≈ 1.0 (for sufficient $k$)
2. $\hat{Q}$ for all-patches = 1.0 by definition
3. $\hat{Q}$ for random < $\hat{Q}$ for edge-density < $\hat{Q}$ for line-drawing (expected ordering)
4. $\hat{Q}$ curves are monotonically increasing with $k$ for all priors
5. Variance across frames is manageable (CI doesn't swallow the signal)


___
## Current Progress

Trying to run offline frame collection, but segfaulting.