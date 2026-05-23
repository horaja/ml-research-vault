## Agenda
1. Review Project Goals
2. Respond/note down any questions
3. Review Next Steps
	1. "What do I need to do to submit SOMETHING by January 26th"
## Notes
1. Overall Project Notes
	1. Dorsal Stream should have 
2. Redirection
	1. V4 Digital Twin (Yingjue)
		1. Model of neural unit as neuronal kernels
			1. ~3000
			2. Half are shape-biased, half not
				1. From Yingjue's paper
	2. "Why do neurons select certain features"
	3. "How are those tokens learned"
		1. What are tokens
			1. prototypes
	4. Use tokens to do patch selection
		1. compimentary/alternative to LD/Depth
			1. Note: LD selects shape-biased boundaries
			2. Note: Depth CAN select boundary (shape) or figure surface (texture)
				1. Note: these two can be complimentary
		2. baseline comparison
			1. Map a token/patch to neuron?
				1. Find the 'most preferred' images for each neuronal unit via the tuning curve for each one
					1. Create this tuning curve from v4 digital twin and ~40k images (STL)
				2. Find the embeddings associated for each of those images and each of those neuronal units via running through vit
					1. Center 'token' embedding out of ViT
				3. Do this for each neuronal unit, 3000 size 'dictionary'
			2. During patch selection, each token will have an embedding
				1. If similar to any embedding in dictionary, they will get selected, otherwise not.
					1. distance/similarity metric below/above some threshold—similar
					2. Thus, throw away patches that are not very 'proto-typical'
				2. Contrastive Learning btwn patch embedding and v4-preferred embeddings.
				3. Which ViT layer closest to this 'V4 representation'?
					1. Previous work? If not, large contribution in and of itself
					2. "Earliest Layer that will produce best result."
					3. Hypothesis: All the layers in front will be processing all patches, all layers behind will not?
				4. Could be a continuous system:
					1. *Hard Constraint*: Current approach
					2. *Soft Constraint*: Linearly interpolate between a full image and minimal representation, based on line drawing intensity (using weak edges/intensity)
						1. Similar strategy for V4 dictionary method?
			3. Baseline: CNN(resnet), v1 visual data(?)
		3. Another contribution: if similar to dpeth/LD performance, claim brain does similar thing
			1. Are the same kinds of patches being selected?
	5. The above can also be used to answer the question: "Which layer is closest to V4 in ViT?"
	6. Application:
		1. Visual Encoders that is more aligned with human-taste/human-preferences
			1. Recommendation Systems
3. Language Model/Language Section influences visual embeddings/selections
	1. Question: Does this circumvent the language model...?
	2. Some kind of top-down attention from language embedding to select specific hypercolumn... via prototypes created from language
		1. Or use last layer of Language Model through a projection/mapping
		2. Or train end-to-end
	3. Learn dictionary via Language-attention bias
	4. Ongoing process over several iterations
	5. Similar to MOCA
4. CLIP Surgery Paper
	1. IDEA: *Test-time skill* - common in language tasks to improve reasoning via added inference time

TASKS via Tiaqin:
1. Set up VLA codebase
2. Ablation study not on P.P. but on FLOPS
3. Fine Tune with color images on Full Model, not just the few layers
	1. Compare with fine-tuned 100% model
	2. Maybe more shape-biased
4. To be more consistent with other baseline, run testing with color images
	1. When doing patch selection, you do black and white and subscaling