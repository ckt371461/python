import tensorflow as tf
#載入資料
(x_train,y_train),(x_test,y_test)=tf.keras.datasets.mnist.load_data() #載入mnist的手寫資料
"""資料處理"""
#1.維度轉換(跟30_2不一樣)
img_rows=x_test.shape[1]
img_cols=x_test.shape[2]
dim=img_rows*img_cols
x_train=x_train.reshape(x_train.shape[0],28,28,1) #轉成(60000, 28,28,1)的矩陣
x_test=x_test.reshape(x_test.shape[0],28,28,1) #轉成(10000, 28,28,1)的矩陣
#2.特徵值增強度(看picture1)
x_train=x_train.astype('float32')
x_test=x_test.astype('float32')
x_train/=255#灰階在0-255之間，所以同除255
x_test/=255
#3.答案轉單熱編碼
y_train=tf.keras.utils.to_categorical(y_train,num_classes=10) #答案有0-9十種
y_test=tf.keras.utils.to_categorical(y_test,num_classes=10)
"""建構模型"""
model=tf.keras.models.Sequential()
model.add(tf.keras.layers.Conv2D( #捲基層 從 1X28X28 變成 3X28X28
    filters=3,#用三個濾鏡產生三個輸出
    kernel_size=(3,3),#捲基層濾鏡大小
    padding='same', #valid填補 或 same 相同
    activation='relu',
    input_shape=(28,28,1)))#圖片大小
model.add(tf.keras.layers.MaxPool2D(pool_size=(2,2)))#池化層 從2X2裡面選出最大值，所以大小變成3X14X14(長寬各一半)
model.add(tf.keras.layers.Conv2D(filters=9,kernel_size=(2,2),padding="same",activation='relu'))#9X14X14(九個輸出，相同大小)
model.add(tf.keras.layers.Dropout(rate=0.33))#丟掉33%的內容避免過度配適
model.add(tf.keras.layers.Flatten())#將2D向量轉維1D的內容
model.add(tf.keras.layers.Dense(units=10,activation='relu')) #使用MLP類神經
model.add(tf.keras.layers.Dense(units=10,activation=tf.nn.softmax))#十種輸出結果
#編譯
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
                loss=tf.keras.losses.categorical_crossentropy,
                metrics=['accuracy'])
model.summary()
#訓練
model.fit(x_train,y_train,epochs=20,batch_size=1024,verbose=1)
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