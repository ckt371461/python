import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
iris = datasets.load_iris()
iris_x_train,iris_x_test,iris_y_train,iris_y_test=train_test_split(iris.data,iris.target,train_size=0.8)

k_means=KMeans(n_clusters=3)#定義時要先說要幾個群，這裡是分成三群
k_means.fit(iris_x_train)

x1=iris_x_train[:,0]#花萼長
y1=iris_x_train[:,1]#花萼寬
plt.scatter(x1,y1,c=k_means.predict(iris_x_train),cmap='viridis')#c是用預測的結果區分顏色，不同顏色代表不同預測結果#cmap是我們要用的調色板
centers=k_means.cluster_centers_
plt.scatter(centers[:,0],centers[:,1],c='black',s=200,alpha=0.5)#alpha是透明度
plt.show()
