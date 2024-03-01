import numpy as np
a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
b=a[0:2,1:3]# 第0,1行，第1,2列
print(a)
print(b)
b[0][0]=99
print(a)#改B，A也會改變，因為是指定同一個pointer
print(b)
#不然要用 a.copy()
c=a[0:2,1:3].copy()
c[0][0]=30
print(a)
print(c)