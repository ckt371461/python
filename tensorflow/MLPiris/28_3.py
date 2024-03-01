#利用Tensorboard來可視化，並且保存訓練結果 
from sklearn import datasets
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

model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),loss=tf.keras.losses.categorical_crossentropy,metrics=['accuracy'])
#tf.keras.optimizers.Adam(lr=0.001)代表用adam每次移動0.001，WARNING:absl:`lr` is deprecated, please use `learning_rate` instead, or use the legacy optimizer, e.g.,tf.keras.optimizers.legacy.Adam.
"""改動"""
from time import time
from tensorflow.keras.callbacks import TensorBoard
tensorboard = TensorBoard(log_dir='log')#放到名為log的資料夾裡
model.fit(x_train, y_train, epochs=200, batch_size=128, callbacks=[tensorboard],verbose=1)#verbose代表訓練完顯示的訊息狀態:0不顯示;1進度;2詳細
'''最後使用tensorboard --logdir=log 指令獲取網址'''
#保存訓練結果 
model_json=model.to_json()
with open('model.json','w') as file:
    file.write(model_json)
model.save_weights('model.h5')

