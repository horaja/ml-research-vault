
### [[02-projects/manifolds/V4-Guided Domain Generalization/Experiments|Experiments]]
- Evaluate **Experiment 1.1 with Brain-Score** metric
- How to **ALIGN**:
	- Optimal transport
- Generalization Task:
	- Additional to *domains*, try **new class**.
- WHAT to **ALIGN**:
	- Actual V4 responses
	- V4 digital twin
		- some units more accurate than others
		- Use pearson correlation threshold

[[Jiang et al. ()]]
#### Neural Response Prediction:
 - Take activation of output of layer3
	 - 1-layer regression/mlp to predict response of 1 neuron at a time, for all neurons - ***TASK***
		 - 3000 Neurons in V4
		 - Error Signal: Use error in tuning curve
	 - Using backprop to update all representations of layers prior to layer3
 - Hypothesis:
	 - Network will change in some way
	 - Better shape-bias, compositional efficiency, etc. etc.
	 - Freeze the layers, fine-tune rest of residual network on object recognition
		 - ***Biologically-Constrained Model***

#### Comparisons
- top-k domain generalization performance

### Specific Literature Review - READ!
[[Dapello et al. (2022)]]
[[Federer et al. (2020)]]
