import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency
categorical = ['WifeEducation','HusbandEducation','WifeReligion','WifeNowWorking','HusbandOccupation','StandardOflivingIndex','MediaExposure']
# 載入數據
df = pd.read_csv('data23combine.csv')
df_targetp = df[df['ContraceptiveMethodUsed'] == 2]
df_p = df_targetp[categorical]
df_targetn = df[df['ContraceptiveMethodUsed'] == 1]
df_n = df_targetn[categorical]
countsp = df_targetp['WifeEducation'].value_counts()
countsn = df_targetn['WifeEducation'].value_counts()
# 計算比例
for col in categorical:
    counts = df_p[col].value_counts()
    proportions = counts / df_p.shape[0]
    print(f'正樣本中{col}的比例:')
    print(proportions)
    
    counts = df_n[col].value_counts()
    proportions = counts / df_n.shape[0]
    print(f'負樣本中{col}的比例:')
    print(proportions)
    c, p, _, _  = chi2_contingency(pd.crosstab(df[col],df['ContraceptiveMethodUsed']))
    print('P值')
    print(p)


