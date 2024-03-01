import matplotlib.pyplot as plt
import numpy as np
#柳丁資料(寬w，長h)
plt.plot([9,9.2,9.6,7.5,6.7,7],[9.4,9.2,9.2,9.2,7.1,7.4],'yx')#黃色叉叉
#橘子資料(寬w，長h)
plt.plot([7.2,7.3,7.2,7.3,7.2,7.3,7.3],[10.3,10.5,9.2,10.2,9.7,10.1,10.1],'gx')#綠色叉叉
plt.plot([7],[9],'r^')#未知物體
circle1=plt.Circle((7,9),1.2,color='#eeeeee')
plt.gcf().gca().add_artist(circle1) #未知物體周邊範圍
plt.axis([6,11,6,11])
plt.ylabel('H cm')
plt.xlabel('W cm')
plt.legend(('Orange','Lemons'),loc='upper right')
plt.show()