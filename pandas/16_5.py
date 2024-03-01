import pandas as pd
data=pd.read_csv('stockThisMonth.csv',sep=',')
print(data[data['日期']>='111/10/08'])#找出特定時間的資料
print(data[(data['日期']>='111/10/08')&(data['日期']<='111/10/15')])#用()括起bool判斷式再用&連接
print(data[['日期','成交筆數']][:5])
print(data.sort_values(by=['成交筆數'])[:5])#找出交易量最少的5筆資料
print(data.sort_values(by=['成交筆數'],ascending=False)[:5])#找出交易量最大的5筆資料
print(data['開盤價'][:15].rolling(5).mean())#取出前五筆資料(包刮自己)做平均