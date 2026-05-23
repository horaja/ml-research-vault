> This metric answers: **"Does our prior attend to the same regions humans attend to during manipulation?"**

This metric complements Option A (reconstruction shift). Option A measures information sufficiency; Option B measures biological plausibility. Together they triangulate: a good prior should score well on both.

---

## The Metric

Given:
- A prior that produces a spatial attention map $A$ from an image
- A human gaze point $g_t = (x, y)$ from the DAA dataset for the same image

**Primary metric — NSS (Normalized Scanpath Saliency):**
$$\text{NSS} = \frac{1}{N} \sum_{i=1}^{N} \frac{A(g_i) - \mu_A}{\sigma_A}$$

Evaluates the attention map directly at gaze locations. NSS > 0 means the prior assigns above-average attention where humans look. No heatmap construction needed for this metric.

**Secondary metric — AUC-Judd:**
Treats $A$ as a binary classifier of fixated vs. non-fixated pixels. Computes ROC curve, returns area under curve. AUC = 0.5 is chance, 1.0 is perfect.

**Tertiary metric — CC (Pearson Correlation):**
Requires constructing a continuous oracle heatmap $H$ from gaze points. Computes correlation between $A$ and $H$. Ranges from -1 to 1.

---

## Data Source: DAA Dataset

### What We Have
The Dual-Action and Attention (DAA) dataset from Kim et al. (2024). 224k episodes of real dual-arm manipulation demonstrations with human gaze tracking.

**Key fields per episode (HDF5 format):**

| Key | Shape | Description |
|-----|-------|-------------|
| `gaze` | (length, 4) | `[left_x, left_y, right_x, right_y]` in pixel coords |
| `left_global_img` | (length, 144, 256, 3) | Wide-angle left camera view |
| `right_global_img` | (length, 144, 256, 3) | Wide-angle right camera view |
| `left_foveated_img` | (length, 320, 360, 3) | High-res crop around gaze |
| `right_foveated_img` | (length, 320, 360, 3) | High-res crop around gaze |
| `desc` | (1,) | Natural language task description (string) |

- Data frequency: **5 Hz**
- 1,104 unique language instructions
- Tasks: pencil-case opening, needle-threading, banana-peeling, bowl-moving, pick, grasp, bottle, place, handkerchief folding, lego, t-shirt, miscellaneous

### Gaze Point Processing
Each frame gives two gaze points (left eye, right eye). For evaluation:
1. **Average** to get single gaze point: $g_t = \frac{1}{2}[(x_L, y_L) + (x_R, y_R)]$
2. **Vergence distance**: $v_t = \|(x_L, y_L) - (x_R, y_R)\|$ — low vergence = precise fixation, high vergence = diffuse attention. Can be used to modulate Gaussian $\sigma$ (see heatmap construction).

### Image Selection
Use `left_global_img` (144×256) as the input image for the prior. This is the wide-angle view that corresponds to the overall scene the human was observing. The foveated images are high-res crops, not suitable as prior input.

**Resolution mismatch**: The prior operates on 224×224 images. The DAA global images are 144×256. You must resize (with padding or center-crop) and remap gaze coordinates accordingly. This is a detail the implementing agent must handle carefully.

---

## High-Level Action Items

### Phase 0: DAA Data Pipeline
- [ ] Download at least 3 task groups from DAA (start with: grasp-and-place, move-bowl, pick — these are closest to BEHAVIOR manipulation tasks)
- [ ] Write HDF5 loader: given a task group directory, iterate over episodes, yield (image, gaze_point, task_description) tuples
- [ ] Handle resolution: resize 144×256 → 224×224, remap gaze pixel coordinates to new resolution
- [ ] Validate: overlay gaze points on images, visually confirm they land on task-relevant objects
- [ ] Filter: discard frames where gaze is outside image bounds or where left/right eye diverge by more than a threshold (likely calibration errors)

### Phase 1: NSS and AUC-Judd Implementation
These metrics operate on raw gaze points — no heatmap construction needed.

**NSS:**
- [ ] Take prior's attention map $A$ (14×14 from patch grid, or upsampled to image resolution)
- [ ] Z-normalize: $A' = (A - \mu_A) / \sigma_A$
- [ ] Sample $A'$ at each gaze location $g_t$
- [ ] Average across all gaze points in the evaluation set
- [ ] Handle edge case: if $\sigma_A = 0$ (uniform attention map), NSS is undefined — report as 0

**AUC-Judd:**
- [ ] Positive set: all gaze locations across frames
- [ ] Negative set: all other pixels (or uniformly sampled subset for efficiency)
- [ ] For each threshold on $A$, compute true positive rate and false positive rate
- [ ] Compute area under the ROC curve
- [ ] Alternative: use sklearn.metrics.roc_auc_score with attention values at gaze points as scores

### Phase 2: Oracle Heatmap Construction (for CC and Visualization)

**Isotropic Gaussian (primary):**
$$H_t(x,y) = \exp\left(-\frac{(x - g_t^x)^2 + (y - g_t^y)^2}{2\sigma^2}\right)$$

For temporal aggregation across a window of $T$ frames:
$$H(x,y) = \frac{1}{T} \sum_{t=1}^{T} H_t(x,y)$$

$\sigma$ values to sweep: [10, 15, 20, 25, 30] pixels (at 224×224 resolution). Report CC at each $\sigma$.

**Vergence-modulated Gaussian (methodological contribution):**
$$\sigma_t = \sigma_{\text{base}} + \alpha \cdot v_t$$

where $v_t = \|(x_L, y_L) - (x_R, y_R)\|$ is the inter-eye distance for frame $t$. When both eyes converge (small $v_t$), $\sigma$ is small → tight fixation. When eyes diverge, $\sigma$ is large → diffuse attention. Set $\sigma_{\text{base}}$ and $\alpha$ via cross-validation or by matching known foveal extent.

### Phase 3: CC Implementation
- [ ] Construct oracle heatmap $H$ (Gaussian, at chosen $\sigma$)
- [ ] Ensure both $A$ and $H$ are at the same resolution
- [ ] Compute Pearson correlation: $\text{CC} = \text{corr}(A.\text{flatten}(), H.\text{flatten}())$
- [ ] Report across multiple $\sigma$ values

### Phase 4: Baseline Priors
Run the same baselines from Option A through Option B's metrics:
1. **Random** attention map: NSS should be ≈ 0, AUC should be ≈ 0.5
2. **Center bias**: NSS and AUC will likely be surprisingly high (humans tend to look near center during manipulation — this is the main confound)
3. **Edge density (Canny)**: structural baseline
4. **Line drawing overlap**: current Module 1 prior

### Phase 5: Evaluation Loop
For each DAA task group, for each prior:
- [ ] Load all episodes
- [ ] For each frame: run prior on image → get $A$, get gaze point $g_t$
- [ ] Compute NSS across all frames
- [ ] Compute AUC-Judd across all frames
- [ ] Compute CC at each $\sigma$ (requires heatmap construction)
- [ ] Report mean ± 95% CI across episodes

---

## Things to Keep in Mind

### Attention Map Resolution
Your prior produces a 14×14 patch-level attention map. NSS and AUC-Judd evaluate at pixel locations. You have two options:
(a) **Upsample** $A$ from 14×14 to 224×224 via bilinear interpolation, then sample at gaze pixel.
(b) **Downsample** gaze point to patch grid (which 16×16 patch does the gaze fall in?), then evaluate at patch level.

Option (a) is standard in saliency evaluation. Option (b) loses spatial precision. Use (a).

### Center Bias Is a Serious Confound
In manipulation tasks, both human gaze and task-relevant objects tend to concentrate near the image center (the robot is looking at its workspace). A center-bias baseline will score well on both Options A and B. Your prior must beat center bias to make any biological plausibility claim. If it doesn't, the result is still publishable (as a negative finding / analysis), but the narrative changes.

### Per-Task vs. Aggregated Metrics
Report metrics per DAA task group AND aggregated. Different tasks have different gaze patterns — needle-threading has extremely concentrated gaze while bowl-moving has distributed gaze. Aggregating masks these differences.

### Option B Does Not Require BEHAVIOR
This entire pipeline runs on DAA data alone. No simulator, no OmniGibson, no Isaac Sim. It can run on any machine with the DAA HDF5 files and your prior model. This is important for development velocity — you can iterate on Option B on a laptop while Option A requires the cluster.

### The Shared Interface with Option A
Both options evaluate the same prior. The prior's interface must be:
```
input: RGB image (224×224×3) → output: attention map (14×14 float)
```
Option A feeds this BEHAVIOR frames and scores via reconstruction quality. Option B feeds this DAA frames and scores via gaze alignment. The implementing agent should ensure this interface is respected so both pipelines can share the same prior objects.

---

## Future Extensions (Not for Now)

- **Phase-conditioned analysis**: Use DAA's `left_dual` / `right_dual` labels to separate "reaching" from "manipulation" phases. Report NSS separately for each phase — the prior's behavior may differ.
- **Task-conditioned analysis**: Group by `desc` and check if the prior performs better on some task types. Does the shape bias from line drawings help more on tasks with distinct object contours (pencil-case) than on amorphous tasks (handkerchief folding)?
- **Temporal coherence**: Measure whether the prior's attention map changes smoothly across frames or jitters. Human gaze is smooth during tracking; prior attention should be too.
- **BEHAVIOR-100 eyetracking validation**: Download the raw VR demos from BEHAVIOR-100, extract eyetracking, and run Option B in-domain for BEHAVIOR scenes.
- **Collect your own gaze data**: Your proposal's Phase 4 mentions human gaze-tracking during manipulation demonstrations in BEHAVIOR. Once collected, this becomes in-domain gaze data that eliminates the DAA-to-BEHAVIOR domain question entirely.

---

## Success Criteria

Option B is working correctly when:
1. Random attention map → NSS ≈ 0, AUC ≈ 0.5
2. Center bias → NSS > 0, AUC > 0.5 (expected, this is the confound to beat)
3. Edge density and line drawing priors → NSS and AUC between random and center bias, or above center bias (if above, that's a strong result)
4. CC is positive for all non-random priors and increases as $\sigma$ increases (larger $\sigma$ → more overlap)
5. Results are consistent across DAA task groups (same ordering of priors)

---

## Dependencies Summary

| Component | Source | Required For |
|-----------|--------|-------------|
| DAA Dataset | https://sites.google.com/view/multi-task-fine | Gaze data + images |
| h5py | `pip install h5py` | Loading DAA HDF5 files |
| scikit-learn | `pip install scikit-learn` | AUC computation |
| scipy | `pip install scipy` | Gaussian kernel, correlation |
| numpy | standard | Everything |
| matplotlib | `pip install matplotlib` | Visualization |
| **No OmniGibson / Isaac Sim required** | | |
