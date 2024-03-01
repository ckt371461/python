import pandas as pd
data=pd.read_html(io='https://mops.twse.com.tw/mops/web/index',header=0)
for i in range(len(data)):
    print(data[i].head())