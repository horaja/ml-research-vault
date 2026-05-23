Goal: Solve the following two problems from [[Disentangled Abstract Representational Learning (DARL) - George Liu]]
1. Ensure Content Encoding represents structure and is separated from Style Encoding
2. Ensure Content Encoding does not catastrophically copy CLIP's embeddings

As explored in [[Manifold Disentanglement Brainstorm]], aligning the manifolds representing the context encoding to the manifolds of the CLIP embeddings could be a promising direction to extract structural semantics (from CLIP's text bias), but also prevent catastrophic copying from CLIP's embeddings.

# Background

Manifold Alignment
 - [[Manifolds]]
 - [@kuochProbingBiologicalArtificial2024]
Domain/Cue Invariance
 - [@wangDiscoveringDomainDisentanglement2022] 
	 - Disentangling domain-invariant features
	 - Uses geometric constraints similar to manifold alignment
- [@bousmalisDomainSeparationNetworks2016]
	- Explicitly Separates domain-invariant and domain-specific features
	- uses reconstruction + adversarial losses *(similar to George's approach)*
	- No Manifold alignment

# Exploring the Idea

What are content, CLIP embeddings, and what are their manifolds?
 - CLIP text manifold
	 - Abstract, Well-Structured, Generalizable
- Content Manifold
	- Set of all structurally relevant encodings across classes, $\gamma$
	- Idea: Ensure relationships between representations of classes are preserved, relative to CLIP's manifolds

How can we align them, and why that method?
 - **Manifold Alignment Loss**
	 - Preserve geometric relationships via *Pairwise Distance Preservation*
		 - Distances - Invariant to rotation/translation & complete geometric description
		 - Dot Product Similarity
		 - PT
		 - Nearest Neighbors Matching
	- Normalization to compare structure, not scale
	- Theory: By preserving the pairwise distances, we preserve the metric, and thus we preserve the manifold structure *(Metric Spaces)*
	- ![[Manifold Structure Preservation]]
	- Prevent sudden collapse

What benefits, what downsides?
 - Benefits
	 - Richer Representations
	 - Better Cross-Domain Transfer
	 - Meaningful Interpolations
- Downsides
	- Computational Complexity - $O(n^2)$
		- Solution: Information Bottleneck -> project to lower dimensionality via PCA
			- CCA *(instead of PCA)* finds dimensions in which the correlation btwn the projection data is maximized <- ensures we only compare relative *stuff?*
			- Same for CLIP's embeddings
	- High Batch Size Required
	- Complex Optimization Landscape
		- Make $n$ distances between classes match these $n$ distances
			- Many ways to satisfy this
		- No guarantees on actual point locations
		- Possible Solution - Combined Loss Term
	- **Semantic Preservation?**
		- How can we relate preserved geometric structure to semantic preservation

How can we test/evaluate?
 - *Manifold Interpolation*—should be semantically smooth.
 - Cross Domain Nearest Neighbors Consistency
 - Style-Swap Invariance
 - Centroid Dispersion Ratio

