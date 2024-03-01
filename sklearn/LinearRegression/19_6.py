
from sklearn import datasets,linear_model
import pandas as pd
import xlsxwriter
diabetes=datasets.load_diabetes()
df=pd.DataFrame(diabetes.data,columns=diabetes.feature_names)
df.to_csv('diabetes.csv',sep=',')
writer=pd.ExcelWriter('diabetes.xlsx',engine='xlsxwriter')
df.to_excel(writer,sheet_name='Sheet1')
writer.close()