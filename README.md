# **SiameseNet Implementation on MNIST**
## Overview

This repository contains a reimplementation of the Siamese Neural Network as described in the original paper:

> *Bromley, Jane, et al. "Signature verification using a 'Siamese' time delay neural network." Advances in Neural Information Processing Systems (1994).*

The goal is to apply Siamese Networks for image similarity learning on the MNIST dataset, where the model learns to determine whether two handwritten digits are the same or different.

Dataset
The MNIST dataset consists of 60,000 training images and 10,000 test images of handwritten digits (0-9).

Model Architecture
The Siamese Network consists of:
- Twin CNN branches sharing weights to extract feature representations from input images.

## Installation & Setup
Clone the repository:
- `git clone https://github.com/sai-srinivasan-v/SiameseNet`

- `cd SiameseNet-MNIST`

## Install dependencies:
- `pip install -r requirements.txt`

## Install dependencies through uv:
- `uv pip install -r requirements.txt`


## Usage
The model can compare two MNIST digits and predict whether they are the same.

## Results
The network learns to distinguish between similar and different digits.


## References
- *Bromley, Jane, et al. "Signature verification using a 'Siamese' time delay neural network."*
- *MNIST Dataset*