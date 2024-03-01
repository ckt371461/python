import tensorflow as tf
#載入資料
(x_train,y_train),(x_test,y_test)=tf.keras.datasets.mnist.load_data() #載入mnist的手寫資料
"""資料處理"""
#1.維度轉換
img_rows=x_test.shape[1]#x_train_shape=(60000, 28, 28)
img_cols=x_test.shape[2]
dim=img_rows*img_cols
x_train=x_train.reshape(x_train.shape[0],dim) #轉成(60000, 784)的矩陣
x_test=x_test.reshape(x_test.shape[0],dim) #轉成(10000, 784)的矩陣
#2.特徵值增強度(看picture1)
x_train=x_train.astype('float32')
x_test=x_test.astype('float32')
x_train/=255#灰階在0-255之間，所以同除255
x_test/=255
#3.答案轉單熱編碼
y_train=tf.keras.utils.to_categorical(y_train,num_classes=10) #答案有0-9十種
y_test=tf.keras.utils.to_categorical(y_test,num_classes=10)

#建構模型
model=tf.keras.models.Sequential()
model.add(tf.keras.layers.Dense(units=10,activation=tf.nn.relu,input_dim=dim)) #784個特徵
model.add(tf.keras.layers.Dense(units=10,activation=tf.nn.relu,kernel_initializer='normal'))#使用normal distribution 常態分佈的亂數定義
model.add(tf.keras.layers.Dense(units=10,activation=tf.nn.softmax)) #十種結果

#編譯
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
                loss=tf.keras.losses.categorical_crossentropy,
                metrics=['accuracy'])
"""查看模型架構"""
model.summary()
#訓練
model.fit(x_train,y_train,epochs=20,batch_size=128,verbose=1)
#測試

print(f'預測:{model.predict(x_test)}')
print(f'實際:{y_test}')
score=model.evaluate(x_test,y_test,batch_size=128)
print(f'score={score}')
#保存訓練結果 
model_json=model.to_json()
with open('model.json','w') as file:
    file.write(model_json)
model.save_weights('model.h5')