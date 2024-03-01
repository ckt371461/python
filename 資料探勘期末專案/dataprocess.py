import pandas as pd

# 讀取 csv 檔案
df = pd.read_csv('data.csv')

# 移除 'ContraceptiveMethodUsed' 值為 2 的行
df = df[df['ContraceptiveMethodUsed'] != 2]

# 將 'ContraceptiveMethodUsed' 值為 3 的行改為 2
df.loc[df['ContraceptiveMethodUsed'] == 3, 'ContraceptiveMethodUsed'] = 2

print(df.head(10))

# 將結果儲存到 data13.csv 檔案中
df.to_csv("data13.csv", index=False)