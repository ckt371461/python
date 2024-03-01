import matplotlib.pyplot as plt
#柳丁資料(寬w，長h)
plt.plot([9,9.2,9.6,7.5,6.7,7],[9.4,9.2,9.2,9.2,7.1,7.4],'yx')#黃色叉叉
#橘子資料(寬w，長h)
plt.plot([7.2,7.3,7.2,7.3,7.2,7.3,7.3],[10.3,10.5,9.2,10.2,9.7,10.1,10.1],'gx')#綠色叉叉
plt.plot([6.5,9.0],[7.8,12.5],'b--')#黑色虛線
plt.ylabel('H cm')
plt.xlabel('W cm')
plt.legend(('Orange','Lemons'),loc='upper right')
'''plt.legend( )中有handles、labels和loc三个参数，其中：

handles需要传入你所画线条的实例对象

labels是图例的名称（能够覆盖在plt.plot( )中label参数值）

loc代表了图例在整个坐标轴平面中的位置（一般选取'best'这个参数值）'''
plt.show()