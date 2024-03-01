import numpy as np

a = np.array([1,2,3])
b = np.array([1,2])

print('a+b=', np.polyadd(a,b))
print('a-b=', np.polysub(a,b))
print('a*b=', np.polymul(a,b))
print('a/b=', np.polydiv(a,b))
