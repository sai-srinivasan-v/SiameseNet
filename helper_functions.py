import numpy as np
import itertools

import matplotlib.pyplot as plt

def plot_images_side_by_side(img_a, img_b, label_a, label_b):
    plt.figure(figsize=(10, 5))
    
    plt.subplot(1, 2, 1)
    plt.imshow(img_a.reshape(28, 28), cmap='gray')
    plt.title(f'Label: {label_a}')
    plt.axis('off')
    
    plt.subplot(1, 2, 2)
    plt.imshow(img_b.reshape(28, 28), cmap='gray')
    plt.title(f'Label: {label_b}')
    plt.axis('off')
    
    plt.tight_layout()
    plt.show()



def make_paired_dataset(X, y):
  X_pairs, y_pairs = [], []

  tuples = [(x1, y1) for x1, y1 in zip(X, y)]
  
  for t in itertools.product(tuples, tuples):
    pair_A, pair_B = t
    img_A, label_A = t[0]
    img_B, label_B = t[1]

    new_label = int(label_A == label_B)

    X_pairs.append([img_A, img_B])
    y_pairs.append(new_label)
  
  X_pairs = np.array(X_pairs)
  y_pairs = np.array(y_pairs)

  return X_pairs, y_pairs