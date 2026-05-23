From [[Disentangled Abstract Representational Learning (DARL) - George Liu]], we have seen a formidable problem statement.

Lets focus on the problem of **Disentanglement**.

# Formalizations

See [[Manifolds]], for a formalization of manifolds.

**Definition 1** *(Disentanglement)*: From [@wangDisentangledRepresentationLearning2024], disentanglement refers to separating underlying factors of variation into variables with semantic meaning.

# [@wangManifoldTransformRecurrent2025]

**Definition 2** *(Concept Manifold)* - One [[Manifolds]] containing all *K* different classes/concepts
- The space where each class has its *canonical* representation

**Definition 3** *(Variants Manifold)* - *K* different [[Manifolds]], one for each class
 - For each concept, contains all different variations of that particular class

# Disentanglement of *Content Encoding* and *Style Encoding*

### Things to Consider:
 - **Manifold Structure Questions**
	 - Relationship between *intrinsic dimensionality* of content and style manifolds
		 - $D_\text{content} \leq D_\text{style}$?
	- Primary Objective: *MANIFOLD ALIGNMENT*
		- Background Literature:
			- Different Problem Statements, other optimizations, etc.
		- Force alignment of content manifolds with *text manifolds*
			- Data source specification for text manifolds.
			- Theory: text manifolds are inherently abstract (no color, texture info); style separation would be a natural byproduct
			- Ensures content encoding doesn't *copy* CLIP embeddings, but rather *aligns* its representation with CLIPs. 

- **Lie Group Properties**; [[Cai et al. (2025)]]
	- *Lie Group Theory*
		- Definition 4 *(Lie Group)*: 
			- A Lie Group is simultaneously
				1. A smooth manifold *(geometric structure)*
				2. A group *(algebraic structure)*
					1. manifolds could have group-based operations that preserve semantic meaning
			 - Collection of **smooth, reversible transformations** that can be combined
		- Definition 5 *(Orbit)*: Set of all points a point can be moved to under the action of the group.
			- e.g. set of all images you can get by applying style transformations to one starting image.
		- Definition 6 *(Quotient)*: $M / G$
			- The set of all orbits
			- *M modulo the action of G.*
		- Definition 7 *(Group Action)*: 
	$$
	\begin{align*}
	\cdot &: G \times M \rightarrow M \\
	(g, x) &\mapsto g \cdot x \\
	\text{where}& \\
	e \cdot x &= x \\
	(g_1 \cdot g_2) \cdot x &= g_1 \cdot (g_2 \cdot x)
	\end{align*}
	$$
	 - *Application* of Lie Group Theory
		 - Recall the $\gamma$ concept manifold and the $\theta$ variants manifolds from [@wangManifoldTransformRecurrent2025]
		 - Consider the following model:
			 - Let a group action $G$ be an accurate model of style transformations on an image, and let $M$ be a set of images.
			 - Then the orbit on an image in $M$ is the set of all the other images in $M$ that can be reached by applying group action $G$ *(style transformations)*
			 - Concepts $\gets$ Orbit *equivalence class*
			 - Style = Group element that moves within orbit
			 - *Quotient* gives you orbit equivalence classes—one representative from each orbit. ![[Lie Group Model]]
