#是否避孕SVM
import numpy as np
from sklearn.metrics import confusion_matrix,classification_report
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import roc_curve, roc_auc_score
import matplotlib.pyplot as plt
"""資料準備"""

df= pd.read_csv('data23combine.csv')
df_target1 = df[df['ContraceptiveMethodUsed'] == 1].sample(500)
df_target2 = df[df['ContraceptiveMethodUsed'] == 2].sample(500)
# 將兩個數據框合併起來
df_balanced = pd.concat([df_target1, df_target2])

x = df_balanced.drop(labels=['ContraceptiveMethodUsed'],axis=1).values 
y = df_balanced['ContraceptiveMethodUsed'] #是否避孕

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2) #切分訓練測試集

"""模型架構及訓練"""
model = svm.SVC(kernel='linear', probability=True)
model.fit(x,y)

"""預測"""
y_predicted =  model.predict(x_test)
print(confusion_matrix(y_test, y_predicted))
print(classification_report(y_test, y_predicted))

# 計算 ROC 曲線的各項參數
fpr, tpr, thresholds = roc_curve(y_test-1, y_predicted-1)

# 計算 AUC 值
auc = roc_auc_score(y_test-1, y_predicted-1)

# 繪製 ROC 曲線
plt.plot(fpr, tpr, label='ROC curve (area = %0.2f)' % auc)
plt.plot([0, 1], [0, 1], 'k--')  # 隨便畫一條對角線
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC')
plt.legend(loc="lower right")
plt.show()