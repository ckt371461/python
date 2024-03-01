import numpy as np
from sklearn.naive_bayes import GaussianNB
x=np.array([[9,9.4],[9.2,9.2],[9.6,9.2],[7.5,9.2],[6.7,7.1],[7,7.4],[7.2,10.3],[7.3,10.5],[7.2,9.2],[7.3,10.2],[7.2,9.7],[7.3,10.1],[7.3,10.1]])
y=np.array([1,1,1,1,1,1,
            2,2,2,2,2,2,2])#1柳丁資料(寬w，長h),2橘子資料(寬w，長h)
model=GaussianNB()
model.fit(x,y)
print(model.class_prior_) #每個分類的機率
print(model.get_params()) #估算工具的參數

x_test=np.array([[8,8],[8.3,8.3]])
predicted=model.predict(x_test)
print(predicted)
print(model.predict_proba(x_test)) #對各分類機率
'''[[1.00000000e+00 3.11797123e-53]前面是柳丁機率，後面是橘子機率
 [1.00000000e+00 2.72385484e-99]]'''

import matplotlib.pyplot as plt
plt.plot(x[:7,0],x[:7,1],'yx')#柳丁
plt.plot(x[7:,0],x[7:,1],'g.')#橘子
plt.plot(x_test[:,0],x_test[:,1],'r^')
plt.xlabel('Weight')
plt.ylabel('Height')
plt.legend(('lemon','orange'))
plt.show()