import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("各縣市歷年戒菸服務人數.csv", encoding='big5')

for i in range(len(df['總計'])): 
    keys=df.keys()[1:]
    for key in keys:
        try:
            df[key][i]=int(df[key][i].replace(',',''))
        except:
            pass
for i in range(len(df['年'])): 
    df['年'][i]=int(df['年'][i][:-1])
print(df[:])


#plt.axis([92,106,20000,200000])

df.plot(x='年',y='總計',kind='box')
plt.legend(('total',))
plt.show()