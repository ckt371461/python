import pandas as pd
data=pd.read_csv('stockThisMonth.csv',sep=',',header=0)
data['漲跌']=data['收盤價']-data['開盤價']
print(data.head())
print(type(data))#資料類型
print(data.shape)#資料大小
print(data.columns)#欄位名稱
print(data.index)#欄位索引
print(data.info())#相關資訊
print(data.describe())#統計描述
'''df.head() / Series.head() 顯示前幾筆資料
df.tail() / Series.tail()顯示最後幾筆資料
df.columns | df.index 顯示所有欄位/索引名稱'''
