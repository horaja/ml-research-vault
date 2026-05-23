See [@DisentangledAbstractRepresentation] for more information.
### Overall Problem Statement
![[Screenshot 2025-11-11 at 1.49.44 AM.png]]
Enhance Vision Models to recognize and perform well under extreme domain shifts during testing, e.g. training on color photos, but evaluating on line-drawing domain images only.

### George's Current Progress
![[Screenshot 2025-11-11 at 1.52.46 AM.png]]
Main Problem: Context Encoding 'copies' CLIP's embeddings, does not create any substantially representative vector itself.