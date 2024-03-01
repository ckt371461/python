'''使用numpy.Ravel(),numpy.linspace(),numpy.meshgrid(x,y)'''
import numpy as np
t1=np.array([[1,2],[3,4]]) 
print(t1.ravel()) #多維變一維
t2=np.linspace(0,10,3)#輸出0到十等分三個數字
print(t2)
t3=np.linspace(0,10,2)#輸出0到十等分2個數字
print(t3)
t4,t5=np.meshgrid(t2,t3) 
'''將兩個矩陣的大小相乘，例如[1,2,3]和[4,5,6]就會變成一個3X3的二維矩陣
第一個數向下擴展，例如[1,2,3]變成[1,2,3]，第二個向右擴展，例如[4,5,6]變成[4,4,4]
                               [1,2,3]                              [5,5,5]
                               [1,2,3]                              [6,6,6]'''
print(t4)
print(t5)
t4,t5=np.meshgrid(t3,t2) 
print(t4)
print(t5)
t6=np.c_[np.array([1,2,3]),np.array([4,5,6])] #合併兩個矩陣，第一個對第一個，第二個對第二個，以此類推
print(t6)
t6=np.c_[np.array([1,2,3]),np.array([4,5,6]),np.array([7,8,9])]
print(t6)