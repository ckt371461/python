import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsRegressor
from sklearn import datasets
import pandas as pd
import xlsxwriter 
iris = datasets.load_iris()
df=pd.DataFrame(iris.data,columns=iris.feature_names)
df['target']=iris.target
writer=pd.ExcelWriter('iris.xlsx',engine='xlsxwriter')
df.to_csv('iris.csv',sep=',')
df.to_excel(writer,sheet_name='sheet1')
writer.close()