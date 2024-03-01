import numpy as np
x=np.array([[-1,2,3],[13,14,15]])
print(x)
print(np.sum(x))#全部數值相加
print(np.sum(x,axis=0))#每列數值相加
print(np.sum(x,axis=1))#每行數值相加
print(np.max(x))#最大
print(np.min(x))#最小
print(np.cumsum(x))#累加陣列，(第1個),(第1個+第2個),(第1個+第2個+第3個)
print(np.mean(x))#平均值
print(np.average(x))#加權平均數，不加權時等於mean
xw=np.array([[0.1,0.2,0.3],[0.4,0.5,0.6]])
print(np.average(x,weights=xw))#以XW加權
print(np.median(x))#中位數，(3和13的平均)
print(np.std(x))#標準差
print(np.var(x))#方差(變異數)
print(x.T)#顛倒

