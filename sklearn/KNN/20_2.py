import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier 
x=[[9,9.4],[9.2,9.2],[9.6,9.2],[7.5,9.2],[6.7,7.1],[7,7.4],[7.2,10.3],[7.3,10.5],[7.2,9.2],[7.3,10.2],[7.2,9.7],[7.3,10.1],[7.3,10.1]]
y=[1,1,1,1,1,1,
   2,2,2,2,2,2,2]#1柳丁資料(寬w，長h),2橘子資料(寬w，長h)
neigh=KNeighborsClassifier(n_neighbors=3)#使用kNN,k=3
neigh.fit(x,y)
print(f'預測答案= {neigh.predict([[7,9]])}' )
print(f'預測樣本距離= {neigh.predict_proba([[7,9]])}' )

