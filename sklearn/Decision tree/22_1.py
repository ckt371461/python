from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import numpy as np
x=np.array([[180,85],[174,80],[170,75], #man身高體重
            [167,45],[158,52],[155,44]]) #woman身高體重
y=np.array(['man','man','man','woman','woman','woman'])
classifier=DecisionTreeClassifier()
classifier.fit(x,y)
prediction=classifier.predict([[173,78]])
print(prediction)

plt.plot(x[:3,0],x[:3,1],'yx')#man
plt.plot(x[3:,0],x[3:,1],'g^')#woman
plt.plot([173],[76],'r.')#預測點
plt.xlabel('Height')
plt.ylabel('Weight')
plt.legend(('man','woman'))
plt.show()