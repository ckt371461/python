import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets,linear_model
diabetes=datasets.load_diabetes()#從datasets裡取得數據
diabetes_x=diabetes.data[:,np.newaxis,2]
#切分x的測試及訓練集
diabetes_x_train=diabetes_x[:-20]#前面拿來訓練
diabetes_x_test=diabetes_x[-20:]#最後20比測試
##切分y的測試及訓練集
diabetes_y_train=diabetes.target[:-20]
diabetes_y_test=diabetes.target[-20:]
#diabetes裡面有:data,target,frame,DESCR,feature_names,data_filename,target_filename,data_module
regr=linear_model.LinearRegression()
regr.fit(diabetes_x_train,diabetes_y_train)

print(f'Coefficient:{regr.coef_}')#相關係數
print(f'Mean Squared error:{np.mean((regr.predict(diabetes_x_test)-diabetes_y_test)**2)}')#方差
print(f'Variance score:{regr.score(diabetes_x_test,diabetes_y_test)}')#變異數

plt.scatter(diabetes_x_test,diabetes_y_test,color='black')
plt.plot(diabetes_x_test,regr.predict(diabetes_x_test),color='blue',linewidth=3)
plt.show()