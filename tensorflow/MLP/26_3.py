#單熱編碼(One-hot Encoding),使用to_categorical()函數
import tensorflow as tf
import numpy as np
#產生隨機的1000筆資料，500筆在0-1之間答案為0,500筆在1-2之間答案為1
x1=np.random.random((500,1)) #500X1矩陣
x2=np.random.random((500,1))+1
x_train=np.concatenate((x1,x2))#把X1和x2結合起來變成500X2的矩陣
y1=np.zeros((500,),dtype=int)
y2=np.ones((500,),dtype=int)
y_train=np.concatenate((y1,y2))

"""改變"""
#將訓練結果轉成單熱編碼，訓練和測試的label要一致，因此都要轉
y_train=tf.keras.utils.to_categorical(y_train,num_classes=2)#兩種答案，轉單熱編碼

#產生模型
model=tf.keras.models.Sequential()
model.add(tf.keras.layers.Dense(units=10,activation=tf.nn.relu,input_dim=1))
model.add(tf.keras.layers.Dense(units=10,activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(units=2,activation=tf.nn.softmax))
"""改變，loss參數也要換"""
#編譯資料
model.compile(optimizer='adam', #編譯處理使用adam最佳化
              loss=tf.keras.losses.categorical_crossentropy,
              metrics=['accuracy'])#設定編譯處理時以準確度為主

#訓練資料
model.fit(x_train,y_train, #訓練的因跟果
            epochs=20, #訓練(機器學習)的次數
            batch_size=128) #每次訓練的筆數
#產生測試資料
x_test=np.array([[0.22],[0.31],[1.22],[1.33]])
y_test=np.array([0,0,1,1])


"""改變"""
#將測試結果轉成單熱編碼，訓練和測試的label要一致，因此都要轉
y_test=tf.keras.utils.to_categorical(y_test,num_classes=2)
#評估要放在編碼後，不然前後格式不一樣會對不上
socre=model.evaluate(x_test,y_test,batch_size=128)
print(f'socre={socre}') #[損失率，正確率]
#預測
predict=model.predict(x_test)
print(f'predict={predict}')#[x1的機率,x2的機率]
#predict_class=model.predict_classes(x_test) #AttributeError: 'Sequential' object has no attribute 'predict_classes'.
predict_class=np.argmax(predict,axis=1)
predict_class=tf.keras.utils.to_categorical(predict_class,num_classes=2)
print(f'預測:{predict_class}')
print(f'實際:{y_test[:]}')
