#是否避孕SVM
import numpy as np
from sklearn.metrics import confusion_matrix,classification_report
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import svm
"""資料準備"""
data= pd.read_csv('data.csv')
x = data.drop(labels=['ContraceptiveMethodUsed'],axis=1).values 
y = data['ContraceptiveMethodUsed'] #是否避孕，1=No-use, 2=Long-term, 3=Short-term
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2) #切分訓練測試集

"""模型架構及訓練"""
rbf = svm.SVC(kernel='rbf', gamma=0.5, C=0.1).fit(x_train, y_train)
poly = svm.SVC(kernel='poly', degree=3, C=1).fit(x_train, y_train)

"""預測"""
y_predicted =  poly.predict(x_test)
print(confusion_matrix(y_test, y_predicted))
print(classification_report(y_test, y_predicted))
