
def sqish(x):    
    u=tf.clip_by_value(x,-2,200)    
    a = u    
    alpha = 1.0    
    at = a + (a*a)/32.0    
    t = alpha*(a + 2*(a*a)/4.0)     
    return tf.maximum(0.0, at) + tf.minimum(0.0,t)
