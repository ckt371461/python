import tensorflow as tf
import numpy as np
#產生隨機的1000筆資料，500筆在0-1之間答案為0,500筆在1-2之間答案為1
x1=np.random.random((500,1)) #500X1矩陣
x2=np.random.random((500,1))+1
x_train=np.concatenate((x1,x2))#把X1和x2結合起來變成500X2的矩陣
y1=np.zeros((500,),dtype=int)
y2=np.ones((500,),dtype=int)
y_train=np.concatenate((y1,y2))

#產生模型
#這樣寫也行
'''model=tf.keras.models.Sequential()
model.add(tf.keras.layers.Dense(units=10,activation=tf.nn.relu,input_dim=1))
model.add(tf.keras.layers.Dense(units=10,activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(units=2,activation=tf.nn.softmax))'''
model=tf.keras.models.Sequential([ #兩層隱藏一層輸出 
    #tf.keras.layers.Flatten(input_shape=(x,y)),
    tf.keras.layers.Dense(units=10,activation=tf.nn.relu,input_dim=1),#隱藏層1
    tf.keras.layers.Dense(units=10,activation=tf.nn.relu),#隱藏層2
    tf.keras.layers.Dense(units=2,activation=tf.nn.softmax)#輸出層，兩種答案
])
'''units：此參數指定層中的神經元數量。 在第一行情況下，層中有10個神經元。
activation：此參數指定激活函數。 在這種情況下，使用了TensorFlow中的relu函數。
input_dim：此參數指定輸入數據的維數。 在這種情況下，輸入數據具有1個維度。'''

'''relu（修正线性单元）是一种常用的神经网络激活函数。 它的输出值为输入值的线性函数，但是当输入值小于0时，输出值为0。
relu函数通常用於隐藏层，并且在解决深度学习问题时非常有效。 它可以有效地防止梯度消失和梯度爆炸的问题，并且还可以加速训练'''

'''tf.nn.softmax是TensorFlow中的一个函数，用于计算输入数据的softmax函数。
Softmax函数是一种常用的多分类激活函数，用于将输入的分数转换为概率值。 它的输出是一个概率分布，其中每个输出值表示相应类别的概率。
Softmax函数通常用作输出层，并且在多分类问题中非常有用。 例如，您可以使用Softmax函数预测图像中物体的类别。'''

'''tf.nn.Flatten是TensorFlow中的一个函数，用于将多维数组拉伸成一维数组。
它是一个常用的层，通常用于将输入数据拉伸成一维数组，以便将它们输入到密集连接层中。'''
#編譯資料
model.compile(optimizer='adam', #編譯處理使用adam最佳化
              loss='sparse_categorical_crossentropy',#損失率處理方式，这是一种常用的损失函数，用于多分类问题。
              metrics=['accuracy'])#設定編譯處理時以準確度為主

#訓練資料
model.fit(x_train,y_train, #訓練的因跟果
            epochs=20, #訓練(機器學習)的次數
            batch_size=128) #每次訓練的筆數
#產生測試資料
x_test=np.array([[0.22],[0.31],[1.22],[1.33]])
y_test=np.array([0,0,1,1])
socre=model.evaluate(x_test,y_test,batch_size=128)
print(f'socre={socre}') #[損失率，正確率]

#預測
predict=model.predict(x_test)
print(f'predict={predict}')#[x1的機率,x2的機率]
#predict_class=model.predict_classes(x_test) #AttributeError: 'Sequential' object has no attribute 'predict_classes'.
predict_class=np.argmax(predict,axis=1)
'''np.argmax是NumPy中的一个函数，用于获取数组中最大值的索引。 它的语法是：
np.argmax(array, axis=None)
其中，array是要查找的数组，axis是要在其中查找最大值的轴。 如果没有指定axis，则会在整个数组中查找最大值。
如果你调用np.argmax(array)，将会返回数组中最大值的索引。
如果你调用np.argmax(array, axis=0)，将会返回每列中最大值的索引，即[0,3]。
如果你调用np.argmax(array, axis=1)，将会返回每行中最大值的索引，即[0,0,1,1]。'''
print(f'預測:{predict_class}')
print(f'實際:{y_test[:]}')