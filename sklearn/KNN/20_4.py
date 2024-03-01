import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets
from sklearn.model_selection import train_test_split #切割資料函示庫
#切割資料80/20
iris=datasets.load_iris()
iris_x_train,iris_x_test,iris_y_train,iris_y_test=train_test_split(iris.data,iris.target,test_size=0.2)#train_size=0.8應該也可
#訓練
knn=KNeighborsClassifier()
knn.fit(iris_x_train,iris_y_train)

print(f'預測: {knn.predict(iris_x_test)}')
print(f'實際: {iris_y_test}')
print(f'準確率: {knn.score(iris_x_test,iris_y_test)}')