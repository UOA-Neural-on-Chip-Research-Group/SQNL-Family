import tensorflow as tf
import numpy as np
import keras

def sqreu(x):    
    u=tf.clip_by_value(x,-2,200)    
    a = u    alpha = 1.0    
    t = alpha*(a + 2.0*(a*a)/4.0)      
    return tf.maximum(0.0, a) + tf.minimum(0.0,t)
