import numpy as np
#大小不同矩陣相加方法
#方法1
x=np.array([[1,2,3],[4,5,6]])
v=np.array([1,0,1])
y=np.empty_like(x)#跟X一樣形狀的空矩陣
for i in range(2):
    y[i,:]=x[i,:]+v
print(y)
#方法2
v2=np.tile(v,(2,1))#行數乘2，列數不變
print(v2)
print(x+v2)
#方法3
print(x+v)