# From Saliency to DINO: Saliency-guided Vision Transformer for Few-shot Keypoint Detection

**Authors:** Changsheng Lu, Hao Zhu, Piotr Koniusz  
**Year:** 2023  
**Venue:**   
[Open in Zotero](zotero://select/items/@luSaliencyDINOSaliencyguided2023)  

---

**Abstract:**  
Unlike current deep keypoint detectors that are trained to recognize limited number of body parts, few-shot keypoint detection (FSKD) attempts to localize any keypoints, including novel or base keypoints, depending on the reference samples. FSKD requires the semantically meaningful relations for keypoint similarity learning to overcome the ubiquitous noise and ambiguous local patterns. One rescue comes with vision transformer (ViT) as it captures long-range relations well. However, ViT may model irrelevant features outside of the region of interest due to the global attention matrix, thus degrading similarity learning between support and query features. In this paper, we present a novel saliency-guided vision transformer, dubbed SalViT, for few-shot keypoint detection. Our SalViT enjoys a uniquely designed masked self-attention and a morphology learner, where the former introduces saliency map as a soft mask to constrain the self-attention on foregrounds, while the latter leverages the so-called power normalization to adjust morphology of saliency map, realizing “dynamically changing receptive field”. Moreover, as salinecy detectors add computations, we show that attentive masks of DINO transformer can replace saliency. On top of SalViT, we also investigate i) transductive FSKD that enhances keypoint representations with unlabelled data and ii) FSKD under occlusions. We show that our model performs well on five public datasets and achieves ~10% PCK higher than the normally trained model under severe occlusions.

---

**My Notes:**  

- 
