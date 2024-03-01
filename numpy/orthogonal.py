import numpy as np
def orthogonal(a,b):
    print(abs(np.dot(a,b)))
    if abs(np.dot(a,b))<0.1:
        return True
    else: return False
k=[1.54681,2]
j=[-2,1.54681]
print(orthogonal(k,j))