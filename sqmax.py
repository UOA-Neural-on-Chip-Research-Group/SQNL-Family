import tensorflow as tf
import numpy as np
import keras
def sqmax(x):  
    return (x*x) / tf.math.reduce_sum((x*x))
