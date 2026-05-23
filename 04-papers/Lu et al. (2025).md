# Reinforcement Learning-based Token Pruning in Vision Transformers: A Markov Game Approach

**Authors:** Chenglong Lu, Shen Liang, Xuewei Wang, Wei Wang  
**Year:** 2025  
**Venue:**   
[Open in Zotero](zotero://select/items/@luReinforcementLearningbasedToken2025)  

---

**Abstract:**  
Vision Transformers (ViTs) have computational costs scaling quadratically with the number of tokens, calling for effective token pruning policies. Most existing policies are handcrafted, lacking adaptivity to varying inputs. Moreover, they fail to consider the sequential nature of token pruning across multiple layers. In this work, for the first time (as far as we know), we exploit Reinforcement Learning (RL) to data-adaptively learn a pruning policy. Formulating token pruning as a sequential decision-making problem, we model it as a Markov Game and utilize Multi-Agent Proximal Policy Optimization (MAPPO) where each agent makes an individualized pruning decision for a single token. We also develop reward functions that enable simultaneous collaboration and competition of these agents to balance efficiency and accuracy. On the well-known ImageNet-1k dataset, our method improves the inference speed by up to 44% while incurring only a negligible accuracy drop of 0.4%. The source code is available at https://github.com/daashuai/rl4evit.

---

**My Notes:**  

- 
