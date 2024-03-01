import numpy as np
a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
row_r1=a[1,:]
row_r2=a[1:2,:]
print(row_r1,row_r1.shape)
print(row_r2,row_r2.shape)
#雖然資料是一樣的，但r1是一維陣列,r2是二維陣列
col_r1=a[:,1]
col_r2=a[:,1:2]
print(col_r1,col_r1.shape)
print(col_r2,col_r2.shape)
