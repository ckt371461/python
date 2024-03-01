from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
import numpy as np
x=np.array([[180,85],[174,80],[170,75], #man身高體重
            [167,45],[158,52],[155,44]]) #woman身高體重
y=np.array(['man','man','man','woman','woman','woman'])
classifier=RandomForestClassifier(n_estimators=100,max_depth=10)#一百組樹木數量，最大深度10層
classifier.fit(x,y)
prediction=classifier.predict([[180,85]])
print(prediction)

