import numpy as np

def sqlu_d(x): # derivative
    alpha = 1.0
    if x > 0.0:
        return 1.0
    elif -2.0<=x and x <=0:
        return alpha*(1 + (x)/2.0)
    else:
        return -1.0
sqlu_d = np.vectorize(sqlu_d)
