import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
data=pd.read_csv('stockThisMonth.csv',sep=',')
x_values=data[['開盤價']].values
y_values=data[['收盤價']].values
'''使用了錯誤的資料類型來進行線性回歸。在使用 scikit-learn 的 LinearRegression 類別進行回歸分析時，
您必須將輸入資料提供給模型作為矩陣，而不是單個向量。
要修正這個問題，您可以使用 Pandas 的 DataFrame.values 屬性將資料轉換為矩陣，然後將其傳遞給 LinearRegression.fit 方法'''

body_reg=linear_model.LinearRegression()
body_reg.fit(x_values,y_values)

plt.scatter(x_values,y_values)
plt.plot(x_values,body_reg.predict(x_values))
plt.show()