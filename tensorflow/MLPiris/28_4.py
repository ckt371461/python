#讀取28_3.py存在model.h5和model.json的訓練結果
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

"""改動"""
#讀取模型架構
json_file=open('model.json','r')
loaded_model_json=json_file.read()
json_file.close()
model=tf.keras.models.model_from_json(loaded_model_json)
#讀取模型權重
model.load_weights('model.h5')
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),loss=tf.keras.losses.categorical_crossentropy,metrics=['accuracy'])

print(f'預測:{model.predict(x_test)}')
print(f'實際:{y_test}')
score=model.evaluate(x_test,y_test,batch_size=128)
print(f'score={score}')