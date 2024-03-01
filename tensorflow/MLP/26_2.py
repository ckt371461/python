#使用keras
from keras.layers import Dense
from keras.models import Sequential
import numpy as np
x1=np.random.random((500,1)) 
x2=np.random.random((500,1))+1
x_train=np.concatenate((x1,x2))
y1=np.zeros((500,),dtype=int)
y2=np.ones((500,),dtype=int)
y_train=np.concatenate((y1,y2))

#改變在這裡
model=Sequential()
model.add(Dense(units=10,activation='relu',input_dim=1))
model.add(Dense(units=10,activation='relu'))
model.add(Dense(units=2,activation='softmax'))

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy',metrics=['accuracy'])

model.fit(x_train,y_train,epochs=20,batch_size=128) 

x_test=np.array([[0.22],[0.31],[1.22],[1.33]])
y_test=np.array([0,0,1,1])
socre=model.evaluate(x_test,y_test,batch_size=128)
print(f'socre={socre}')

predict=model.predict(x_test)
print(f'predict={predict}')
predict_class=np.argmax(predict,axis=1)
print(f'預測:{predict_class}')
print(f'實際:{y_test[:]}')