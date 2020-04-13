import numpy as np

def sqnl(x):
    m = 2
    
    def inner(x):
        x_clip = np.clip(x, -m, m)
        if x_clip >= 0:
            return x_clip - (x_clip * x_clip)/4.0
        else:
            return x_clip + (x_clip * x_clip)/4.0
    
    sqnl_inner = np.vectorize(inner)
    return sqnl_inner(x)
