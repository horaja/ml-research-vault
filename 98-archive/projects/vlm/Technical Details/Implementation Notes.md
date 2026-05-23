For overall Project Summary, see [[Project Overview - DISCONTINUED]].
For specific experiments ran, see [[Implementation Notes]].
## Dorsal Stream
### Shape-Bias Incorporation
#### Line Drawing Generation
 - LD Style: **contour**
	 - Most biologically-accurate, no outside biases, cleanest

#### Magno-Style Transform
 - Gray-Scale
 - Strong Gaussian Blur *(aniti-aliasing filter)* + Subsampling
 - Apply non-linear contrast response - [[Kaplan et al. (1986)]]
	 - Enhance Low Contrast, Saturate High Contrast

## TOKEN MERGING

[[Bolya et al. (2023)]]
Instead of direct pruning, merge tokens together.
Key Idea: Tokens merged **BEFORE EVERY TRANSFORMER LAYER**. Use this idea!

#### Depth Map & FG/BG Segmentation - [Phase 2] in [[98-archive/projects/vlm/Experiments|Experiments]]
**Background Notes**:
 - Explicitly separating foregrounds and background enhances ViT training and reduces biases [[Nauen et al. (2025)]]
 - Explicitly doing figure-ground segmentation increases shape-bias of the model --> better robustness and accuracy *[find source]*
 - **Depth Guided Vision Transformers**: NF-DVT uses normalizing flows to build priors for depth maps [[Pan et al. (2024)]]
 - Saliency Maps used to constrain self-attention on foregrounds
	 - Morphology Learner to adapt Saliency [[Lu et al. (2023)]]
	 - SGDViT - Saliency Guided Dynamic ViT - *VERY SIMILAR* [[Yao et al. (2023)]]

**Background Info on Depth Detection**:
 - Depth Continuity = Object Coherence
 - Depth Discontinuities = Object Boundaries
 - Depth Gradients = Surface Orientation
 - Depth Ordering = Occlusion Relationships

**Depth Segmentation**:
- Depth Anything V2 Small
	- ~25M parameters
- DINO Backbone

**Depth Map**:
- Lite Mono
	- ~3M parameters
	- input: 256x256 color
		- anything else, most likely will not work
	- output: disparity map
		- high values -> close, low values -> far
- SwiftDepth++
#### Proposed Approaches:
1. Simplest: **Depth Discontinuity Boundaries**:
	1. Create a *soft-boundary*
2. **Multi-modal importance scorer**
	1. Combines
		1. LD Density
		2. FG/BG Segmentation masks
		3. Depth Discontinuity maps
	2. **Replace PatchImportanceScorer**
3. **Depth Aware Spatial Bias**
	1. *Correlation Bias* - Anisotropic Weighting - Depth Stratified Attention
		1. Patches at similar depths receive higher correlation bias
	2. Replace 2D Gaussian with depth-aware **kernel**:
		1. $Weight(patch_i, patch_j) = exp(-||p_i - p_j||²/σ_{2d}) × exp(-|d_i - d_j|²/σ_{depth})$
	3. **Enhance SpatialThresholdSelector**
4. **Cross Attention Combining Parallel Streams**
	1. Stream 1: Line drawings → edge importance
	2. Stream 2: Segmentation → semantic importance
	3. Stream 3: Depth → spatial importance
	4. ***TODO***
5. **Depth-Ordered Patch Selection**
	1. Split FG/MG/BG into *bins*. Only select patch up to certain allocation limits for each layer *bin*.
		1. Guarantees FG representation, robust to BG complexity
		2. No learning mechanism
	2. *What do I want to change?*
6. **Learned *Semantic* Multiplier**
	1. Use a Depth Map Prior and Segmentation to learn a semantic multiplier for each patch.
	2. *Architecture?*
		1. MLP?
		2. CNN?
7. **Self-Attention Guided Semantic Importance** [[Lu et al. (2023)]]
	1. Run Lightweight Network to generate importance maps
	2. Sources:
		1. LD
		2. Depth Maps
		3. FG/BG Segmentation Info
#### [[98-archive/projects/vlm/Experiments#*[TODO]* Experiment 2.1 Augment Patch Selector Module with Depth Awareness|Experiments]] - Details
- **Option 1**: 3D Gaussian Kernel
```
def adaptive_depth_cog(disparity_map, line_drawing):
    # Find COG in depth space (not just 2D)
    depth_weighted_cog = compute_3d_centroid(disparity_map, line_drawing)
    
    # Create 3D Gaussian kernel
    weight = exp(-||p_i - cog_3d||² / σ_3d)
    
    # Adaptive sigma based on depth variance
    σ_3d = adjust_sigma_by_depth_variance(disparity_map)
```
- **Option 2**: Depth-Conditioned Importance Score
	- $\alpha$ - controls foreground bias
	- $\beta$ - penalizes patches with high depth variance (spanning multiple depth levels) <- Don't we want the opposite of this...?
```
importance_score = ld_score * (1 + α * disparity_value) * exp(-β * depth_variance)
```

- **Option 3**: Depth allocation 'bins'
```
def hierarchical_depth_selection(disparity_map, line_drawing_scores, num_patches):
    # Stratify patches into depth bins (foreground, midground, background)
    depth_bins = np.percentile(disparity_map, [70, 40, 10])  # High disparity = close
    
    # Allocate patches proportionally: 60% FG, 30% MG, 10% BG
    allocation = {'fg': 0.6, 'mg': 0.3, 'bg': 0.1}
    
    # Select top-scoring patches within each depth layer
    selected_patches = []
    for layer, ratio in allocation.items():
        layer_patches = get_patches_in_depth_range(layer)
        n_select = int(num_patches * ratio)
        selected_patches.extend(
            top_k_patches(layer_patches, line_drawing_scores, n_select)
        )
```
- **Option 4**: Learned Attention Gating Module

***Keep in mind***: Use Meta's SAM3D to create datasets.
