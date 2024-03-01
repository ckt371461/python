import numpy as np
import matplotlib.pyplot as plt
from sklearn import tree
import pydot
from six import StringIO
x=np.array([[180,85],[174,80],[170,75], #man身高體重
            [167,45],[158,52],[155,44]]) #woman身高體重
y=np.array(['man','man','man','woman','woman','woman'])
classifier=tree.DecisionTreeClassifier()
classifier.fit(x,y)

tree.export_graphviz(classifier,out_file='tree.dot')#圖片轉dot

dot_data = StringIO()
tree.export_graphviz(classifier, out_file=dot_data) # dot 轉圖片
graph = pydot.graph_from_dot_data(dot_data.getvalue())
graph[0].write_png('tree.png')