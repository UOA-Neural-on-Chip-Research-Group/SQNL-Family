import tensorflow as tf
import numpy as np
import keras

def sqsoftplus(x):
    u=tf.clip_by_value(x,-0.5,255)
    a = u
    t = ((a+0.5)**2)/2.0 
    cond = tf.greater(a,tf.constant(0.0))
    return tf.where(cond, a, t)
