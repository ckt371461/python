import pandas as pd
df=pd.read_csv('stockThisMonth.csv',sep=',')
df['漲跌']=df['收盤價']-df['開盤價']
#df['日']=pd.DatetimeIndex(df['日期']).year #這裡我們用明國年會有越界纳秒时间戳的問題，因為西元111年不在他的處理範圍之內
#pandas._libs.tslibs.np_datetime.OutOfBoundsDatetime: Out of bounds nanosecond timestamp: 111-10-03 00:00:00 present at position 0
print(df[:])
import matplotlib.pyplot as plt
#df.plot(x='日期',y='漲跌',grid=True,color='blue')#grid是二維的網格系統
#df.plot(y='漲跌',grid=True,color='blue',kind='hist') #直方圖
fields=['開盤價','收盤價']
fig,ax=plt.subplots()#畫布以及區塊的劃分
for name in fields:
    df.plot(x='日期',y=name,ax=ax,label=name)

plt.show()