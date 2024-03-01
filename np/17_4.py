import numpy as np
a=np.array([[1,2],[3,4],[5,6]])
print(a[0][0])
print(a[1][1])
b=[a[0][0],a[1][1]]
print(b)
b=a[[0,1,2],[1,1,0]] #是指a的(0,1)(1,1)(2,0)
print(b)
print(b[1])