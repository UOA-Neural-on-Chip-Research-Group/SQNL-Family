# Derivative of SQNL function
import numpy as np

def sqnl_d(x):
    m = 2
    
    def inner(x):
        x_clip = np.clip(x, -m, m)
        if x_clip >= 0:
            return 1 - (x_clip)/2.0
        else:
            return 1 + (x_clip)/2.0
    
    sqnl_inner = np.vectorize(inner)
    return sqnl_inner(x)
