# **SiameseNet Implementation on MNIST**

## Overview

This repository contains a reimplementation of the **Siamese Neural Network** as described in the original paper:  

> *Bromley, Jane, et al. "Signature verification using a 'Siamese' time delay neural network." Advances in Neural Information Processing Systems (1994).*

The goal is to apply **Siamese Networks** for **image similarity learning** on the **MNIST dataset**, where the model learns to determine whether two handwritten digits are the same or different.

---

## 📂 Dataset  

The **MNIST dataset** consists of:  
- **60,000 training images**  
- **10,000 test images**  
Each image is a **28×28 grayscale handwritten digit** (0-9).  

---

## 🏗 Model Architecture  

The **Siamese Network** consists of:  
- **Twin CNN branches** sharing weights to extract feature representations from input images.  
- **Contrastive loss function** to optimize for similarity learning.  

---

## ⚡ Installation & Setup  

### Clone the Repository  
```bash
git clone https://github.com/sai-srinivasan-v/SiameseNet
cd SiameseNet-MNIST
pip install -r requirements.txt
```
- Using uv
```bash
git clone https://github.com/sai-srinivasan-v/SiameseNet
cd SiameseNet-MNIST
uv pip install -r requirements.txt
```
---

##📊 Results
The network learns to distinguish between similar and different digits, demonstrating the effectiveness of contrastive learning in a low-data regime.


## 📖 References
- Bromley, Jane, et al. "Signature verification using a 'Siamese' time delay neural network."
- LeCun, Yann, et al. "Gradient-based learning applied to document recognition." Proceedings of the IEEE (1998).
- ['MNIST Dataset'](http://yann.lecun.com/exdb/mnist/)
