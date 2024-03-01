import numpy as np
import tensorflow as tf
#建立更複雜的數據庫
def creat_datasets(high,num,arraysize):#(答案數量,要產生的數量,數據維度)
    x=np.random.random((num,arraysize))*float(high)#產生一個取值範圍在0-high之間的浮點數二維陣列(num X arraysize)
    y=((sum(x[:num,i] for i in range(arraysize)))/arraysize).astype(int)#取平均數的整數作為標籤答案
    return x,tf.keras.utils.to_categorical(y,num_classes=high)
#資料
dim=2
category=10
x_train,y_train=creat_datasets(category,1000,dim) #產生一個有十種答案，兩個標籤的一千筆訓練資料
x_test,y_test=creat_datasets(category,10,dim) #產生一個有十種答案，兩個標籤的十筆測試資料
#模型
model=tf.keras.models.Sequential()
model.add(tf.keras.layers.Dense(units=10,activation=tf.nn.relu,input_dim=dim))
model.add(tf.keras.layers.Dense(units=10,activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(units=category,activation=tf.nn.softmax))
#編譯
model.compile(optimizer='adam',loss=tf.losses.categorical_crossentropy,metrics=['accuracy'])
#訓練
model.fit(x_train,y_train,epochs=200,batch_size=64)
#測試
predict=model.predict(x_test)
print(f'predict={predict}')
predict_class=np.argmax(predict,axis=1)
print(f'預測:{predict_class}')
print(f'實際:{y_test[:]}')
socre=model.evaluate(x_test,y_test,batch_size=128)
print(f'socre={socre}')
"""結果:預測成功率很低，還需再調整[1.9867727756500244, 0.20000000298023224]，正確率僅0.2左右"""
#1. 將epochs從20提升為200，[1.154465675354004, 0.699999988079071]，正確率提升至0.7左右
#2. 將batch_size從128降至64，增加總訓練次數，0.43653759360313416, 0.8999999761581421]，正確率提升至0.9左右
"""缺點:訓練時間相較於一開始長了很多"""