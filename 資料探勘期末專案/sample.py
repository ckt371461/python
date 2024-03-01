import pandas as pd
df = pd.read_csv('data23combine.csv')
# 對於每個分類目標，使用 sample() 方法從數據框中隨機抽樣，抽出 500 筆樣本
df_target1 = df[df['ContraceptiveMethodUsed'] == 1].sample(500)
df_target2 = df[df['ContraceptiveMethodUsed'] == 2].sample(500)
# 將兩個數據框合併起來
df_balanced = pd.concat([df_target1, df_target2])
print(df[df['ContraceptiveMethodUsed']==1].value_counts) #628筆資料
print(df[df['ContraceptiveMethodUsed']==2].value_counts) #844筆資料
