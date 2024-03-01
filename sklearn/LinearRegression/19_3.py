import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
x_value=pd.DataFrame([0,1,2])#訓練資料
y_value=pd.DataFrame([0,0.3,0.6])
x_test=pd.DataFrame([-1,3,5])#測試資料

body_reg=linear_model.LinearRegression()#指定線性回歸
body_reg.fit(x_value,y_value)      #訓練

y_test_predict=body_reg.predict(x_test)
print(y_test_predict)

plt.scatter(x_value,y_value,color='blue')
plt.scatter(x_test,y_test_predict,color='red')
plt.plot(x_test,y_test_predict,color='black')
plt.show()