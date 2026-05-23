# Think Twice to See More: Iterative Visual Reasoning in Medical VLMs

**Authors:** Kaitao Chen, Shaohao Rui, Yankai Jiang, Jiamin Wu, Qihao Zheng, Chunfeng Song, Xiaosong Wang, Mu Zhou, Mianxin Liu  
**Year:** 2025  
**Venue:**   
[Open in Zotero](zotero://select/items/@chenThinkTwiceSee2025)  

---

**Abstract:**  
Medical vision-language models (VLMs) excel at image-text understanding but typically rely on a single-pass reasoning that neglects localized visual cues. In clinical practice, however, human experts iteratively scan, focus, and refine the regions of interest before reaching a final diagnosis. To narrow this machine-human perception gap, we introduce ViTAR, a novel VLM framework that emulates the iterative reasoning process of human experts through a cognitive chain of "think-act-rethink-answer". ViTAR treats medical images as interactive objects, enabling models to engage multi-step visual reasoning. To support this approach, we curate a high-quality instruction dataset comprising 1K interactive examples that encode expert-like diagnostic behaviors. In addition, a 16K visual question answering training data has been curated towards fine-grained visual diagnosis. We introduce a two-stage training strategy that begins with supervised fine-tuning to guide cognitive trajectories, followed by the reinforcement learning to optimize decision-making. Extensive evaluations demonstrate that ViTAR outperforms strong state-of-the-art models. Visual attention analysis reveals that from the "think" to "rethink" rounds, ViTAR increasingly anchors visual grounding to clinically critical regions and maintains high attention allocation to visual tokens during reasoning, providing mechanistic insight into its improved performance. These findings demonstrate that embedding expert-style iterative thinking chains into VLMs enhances both performance and trustworthiness of medical AI.

---

**My Notes:**  

- 
