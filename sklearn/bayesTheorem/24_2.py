import numpy as np
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB
x=np.array([[9,9.4],[9.2,9.2],[9.6,9.2],[7.5,9.2],[6.7,7.1],[7,7.4],[7.2,10.3],[7.3,10.5],[7.2,9.2],[7.3,10.2],[7.2,9.7],[7.3,10.1],[7.3,10.1]])
y=np.array([1,1,1,1,1,1,
            2,2,2,2,2,2,2])#1柳丁資料(寬w，長h),2橘子資料(寬w，長h)
model=GaussianNB()
model.fit(x,y)
plt.plot(x[:7,0],x[:7,1],'yx')#柳丁
plt.plot(x[7:,0],x[7:,1],'g.')#橘子
plt.xlabel('Weight')
plt.ylabel('Height')
plt.legend(('lemon','orange'))
x_min=x[:,0].min()-0.5
x_max=x[:,0].max()+0.5
y_min=x[:,1].min()-0.5
y_max=x[:,1].max()+0.5
xx,yy=np.meshgrid(np.linspace(x_min,x_max,30),np.linspace(y_min,y_max,30))#x跟y都各自切成30格再展開
z=model.predict_proba(np.c_[xx.ravel(),yy.ravel()])#形成一個900X2的向量,裡面的內容是柳丁和橘子各自的機率['柳丁','橘子']
z1=z[:,1].reshape(xx.shape) #這裡用[:,0]或[:,1]都可，但要注意下一行的判斷式的機率要選哪個，0要用柳丁機率，1要用橘子機率
plt.contour(xx,yy,-z1,[-0.5],colors='k') #劃出檸檬和柳丁機率為50:50的等高線(用-z1判斷，所以是[-0.5])
plt.savefig('myBayes.png',bbox_inches='tight')
plt.show()