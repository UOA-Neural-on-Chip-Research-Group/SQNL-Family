# Derivative of log_sqnl
import numpy as np

def log_sqnl_d(x):
    m = 2
    
    def inner(x):
        x_clip = np.clip(x, -m, m)
        if x_clip >= 0:
            return (2 - x_clip )/4.0
        else:
            return (2 + x_clip )/4.0
    
    sqnl_inner = np.vectorize(inner)
    return sqnl_inner(x)
