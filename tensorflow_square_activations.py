
import keras
import numpy as np
from keras.utils.generic_utils import get_custom_objects
import tensorflow as tf

#Define activation functions
def tf_log_sqnl(x):
    u=tf.clip_by_value(x,-2,2)
    a = u
    b= tf.negative(tf.abs(u))
    wsq = (tf.multiply(a,b))/4.0
    y = tf.add(tf.multiply(tf.add(u,wsq),0.5),0.5)
    return y
get_custom_objects().update({'custom_activation': Activation(tf_log_sqnl)})

def tf_sqnl(x): 
    u=tf.clip_by_value(x,-2,2)
    a = u
    b= tf.negative(tf.abs(u))
    wsq = (tf.multiply(a,b))/4.0
    y = tf.add(u,wsq)
    return y
get_custom_objects().update({'custom_activation': Activation(tf_sqnl)})


def tf_sqlu(x):
    u=tf.clip_by_value(x,-2,200)
    a = u
    alpha = 1.0
    t = alpha*(a + (a*a)/4.0) 
    cond = tf.greater(a,tf.constant(0.0))
    return tf.where(cond, a, t)
get_custom_objects().update({'custom_activation': Activation(tf_sqlu)})


def tf_sqsoftplus(x):
    u=tf.clip_by_value(x,-0.5,255)
    a = u
    t = ((a+0.5)**2)/2.0 
    cond = tf.greater(a,tf.constant(0.0))
    return tf.where(cond, a, t)
get_custom_objects().update({'custom_activation': Activation(tf_sqsoftplus)})
