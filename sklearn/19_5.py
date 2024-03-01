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

print(f'Coefficient:{regr.coef_}')
print(f'Mean Squared error:{np.mean((regr.predict(diabetes_x_test)-diabetes_y_test)**2)}')
print(f'Variance score:{regr.score(diabetes_x_test,diabetes_y_test)}')
'''LinearRegression.coef_ 屬性：這個屬性包含了模型中所有輸入變量的系數，它可以用來反映輸入變量對輸出變量的影響程度。
np.mean 函數：這個函數會計算預測值和實際值之間的差異，並計算它們的平方和的平均值，這被稱為均方差（mean squared error）。均方差越小，模型的表現就越好。
LinearRegression.score 方法：這個方法可以計算預測值和實際值之間的相關性。它的輸出值介於 0 和 1 之間，越接近 1 表示模型的表現越好。'''

plt.scatter(diabetes_x_test,diabetes_y_test,color='black')
plt.plot(diabetes_x_test,regr.predict(diabetes_x_test),color='blue',linewidth=3)

plt.show()