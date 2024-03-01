from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
import numpy as np
x,y=make_classification(n_samples=10,     #10筆資料
                        n_features=3,       #每筆三個特徵
                        n_informative=2,    #兩種答案
                        n_redundant=0,      #沒有過剩值
                        random_state=0,     #確定數據及創建的隨機數生成，random_state 參數是隨機數生成器的種子，如果設定相同的 random_state 就會產生相同的模擬資料
                        shuffle=True)        #亂數排列
classifier=RandomForestClassifier(n_estimators=100,max_depth=10,random_state=2)#random_state 參數是隨機數生成器的種子
classifier.fit(x,y)
print(classifier.feature_importances_) #答案出現比率
print(classifier.predict([[0,0,0]]))    #預測

estimator=classifier.estimators_[5]
'''classifier.estimators_ 屬性包含了隨機森林中的所有決策樹。這個程式碼會取出隨機森林中第 6 棵決策樹，並將它存在 estimator 變數中。
您可以通過改變 [5] 中的數字來取出隨機森林中的不同決策樹'''
from sklearn.tree import export_graphviz
export_graphviz(estimator,out_file='tree.dot',
                feature_names=['a','b','c'], #三個特徵的名稱
                class_names=['1','2'],  #兩個答案的名稱
                rounded = True,proportion=False, #顯示比例
                precision=2,filled=True)  #精確度設定
'''rounded 參數決定是否將葉子節點的標籤轉換為四捨五入的值。proportion 參數決定是否要在每個葉子節點上顯示該節點所屬的類別的比例。
precision 參數表示在四捨五入標籤值時使用的精確度。filled 參數決定是否使用填色的方式顯示節點。'''
# dot -Tpng tree.dot -o tree.png -Gdpi=60  用這個指定將dot檔案 轉為png檔案
