import tensorflow as tf
from tensorflow.keras.models import *
from tensorflow.keras.layers import *

def get_cnn_block(depth):
  return Sequential([Conv2D(depth, 3, 1),
                     BatchNormalization(),
                     ReLU()])