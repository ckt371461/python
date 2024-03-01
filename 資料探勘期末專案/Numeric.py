import numpy as np
import pandas as pd
from scipy.stats import ttest_ind
Numeric = ['WifeAge','NumberOfChildrenEverBorn']
# 載入數據
df = pd.read_csv('data23combine.csv')
df_targetp = df[df['ContraceptiveMethodUsed'] == 2]
df_p = df_targetp[Numeric]
df_targetn = df[df['ContraceptiveMethodUsed'] == 1]
df_n = df_targetn[Numeric]
# 計算所有特徵的標準差，平均數以及P值
stdp = np.std(df_p)
meanp = np.mean(df_p)
stdn = np.std(df_n)
meann = np.mean(df_n)
t, p = ttest_ind(df_p, df_n)


print('Postive')
print('std')
print(stdp)
print('mean')
print(meanp)

print('Negative')
print('std')
print(stdn)
print('mean')
print(meann)
print('PValue')
print(p)