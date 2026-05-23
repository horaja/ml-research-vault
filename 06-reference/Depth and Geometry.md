## Neuroscience of Depth and Attention
- **Ovoid Geometry**:
	- Spatial envelope of attention focus is best described as a 3D ovoid.
	- Thus, spatial weights should be ellipsoid's stretched along the depth axis.
	- [[Caziot et al. (2023)|"We mapped the 3D shape of attentional focus over time and found that the spatial envelope was approximately a Gaussian modulated in time."]]
	- Depth information is available **immediately** to the attention control stream (likely the dorsal stream).
- **Temporal Modulation**: Attention shifts from fovea to periphery over time
- **Area 8av Control**: Top down gain control of sensory input
## Depth-Guided Token Selection
- **ToSA**: [[Huang et al. (2025)]]
	- Uses a dynamically weighted (depending on the layer in ViT) spatial token that is incorporated into the merging logic.
	- Impact: It prevents the fusion of tokens that are semantically similar but spatially distinct
	- Improves upon [[Implementation Notes#^e2156e|Canonical Token Merging]]