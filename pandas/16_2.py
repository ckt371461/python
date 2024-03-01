import pandas as pd
import numpy as np
data=pd.read_csv('stockThisMonth.csv',sep=',',header=0)
print(data.head(len(data)))
print(data['成交筆數'])
print(data[['開盤價','收盤價']]) #兩個以上要用陣列括起來
df=pd.DataFrame({'math':[i for i in range(5)],'english':np.arange(0,5,1)})
print(df[['math','english']])


