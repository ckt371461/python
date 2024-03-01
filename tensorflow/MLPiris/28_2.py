from sklearn import datasets
#圖形化顯示訓練過程
from sklearn.model_selection import train_test_split
import tensorflow as tf
import numpy as np

iris=datasets.load_iris()
category=3 #有三種花
feature=4 #四種特徵
x_train,x_test,y_train,y_test=train_test_split(iris.data,iris.target,test_size=0.2)
y_train=tf.keras.utils.to_categorical(y_train,num_classes=category)
y_test=tf.keras.utils.to_categorical(y_test,num_classes=category)

model=tf.keras.models.Sequential()
model.add(tf.keras.layers.Dense(units=10,activation=tf.nn.relu,input_shape=(4,)))
model.add(tf.keras.layers.Dense(units=10,activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(units=3,activation=tf.nn.softmax))

model.compile(optimizer=tf.keras.optimizers.Adam(lr=0.001),loss=tf.keras.losses.categorical_crossentropy,metrics=['accuracy'])
#tf.keras.optimizers.Adam(lr=0.001)代表用adam每次移動0.001

history=model.fit(x_train,y_train,epochs=200,batch_size=128) #要指定存在history待會才有東西可以畫，不然不會把過程記錄下來
'''history = tf.keras.callbacks.History() #或者改用這樣
model.fit(x_train, y_train, epochs=200, batch_size=128, callbacks=[history])'''
"""改動"""
import matplotlib.pyplot as plt
plt.plot(history.history['accuracy'])
plt.plot(history.history['loss'])
plt.title('score')
plt.xlabel('epoch')
plt.ylabel('acc&loss')
plt.legend(['accuracy','loss'])
plt.show()