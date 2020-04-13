import numpy as np

def sqlu(x):
    alpha = 1.0
    if x > 0.0: #positive part
        return x
    elif -2.0<=x and x <=0: #negative part
        return alpha*(x + (x*x)/4.0) 
    else: #clipping the other negative part to -1.0, anythin less than -2.0
        return -1.0


sqlu = np.vectorize(sqlu)
