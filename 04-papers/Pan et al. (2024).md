# Depth-Guided Vision Transformer With Normalizing Flows for Monocular 3D Object Detection

**Authors:** Cong Pan, Junran Peng, Zhaoxiang Zhang  
**Year:** 2024  
**Venue:**   
[Open in Zotero](zotero://select/items/@panDepthGuidedVisionTransformer2024)  

---

**Abstract:**  
Monocular 3D object detection is challenging due to the lack of accurate depth information. Some methods estimate the pixel-wise depth maps from off-the-shelf depth estimators and then use them as an additional input to augment the RGB images. Depth-based methods attempt to convert estimated depth maps to pseudo-LiDAR and then use LiDAR-based object detectors or focus on the perspective of image and depth fusion learning. However, they demonstrate limited performance and efficiency as a result of depth inaccuracy and complex fusion mode with convolutions. Different from these approaches, our proposed depth-guided vision transformer with a normalizing flows (NF-DVT) network uses normalizing flows to build priors in depth maps to achieve more accurate depth information. Then we develop a novel Swin-Transformer-based backbone with a fusion module to process RGB image patches and depth map patches with two separate branches and fuse them using cross-attention to exchange information with each other. Furthermore, with the help of pixel-wise relative depth values in depth maps, we develop new relative position embeddings in the cross-attention mechanism to capture more accurate sequence ordering of input tokens. Our method is the first Swin-Transformer-based backbone architecture for monocular 3D object detection. The experimental results on the KITTI and the challenging Waymo Open datasets show the effectiveness of our proposed method and superior performance over previous counterparts.

---

**My Notes:**  

- 
