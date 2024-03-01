import numpy as np 
x=np.array([[1,2],[3,4]])
y=np.array([[5,6],[7,8]])
print(x+y)
print(np.add(x,y))
print(x+10)

print(x-y)
print(np.subtract(x,y))
print(x-[1,2])

print(x*y)
print(np.multiply(x,y))#每一格相乘，不是矩陣乘法

print(x/y)
print(np.divide(x,y))#每一格相除

print(x**2)
print(np.square(x))#每一格平方

print(x.dot(y))#矩陣乘法
print(np.dot(x,y))