#製作手寫辨識系統
import cv2
import numpy as np
import tensorflow as tf
'''預測'''
json_file=open('..\\CNN\\model.json','r')
loaded_model_json=json_file.read()
json_file.close()
model=tf.keras.models.model_from_json(loaded_model_json)
#讀取模型權重
model.load_weights('..\\CNN\\model.h5')
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),loss=tf.keras.losses.categorical_crossentropy,metrics=['accuracy'])
"""預測函數"""
def CNN():
    b=img.astype(dtype=np.float32) #資料轉換成浮點數
    x_test=b.reshape((1,28,28,1))
    x_test/255
    predict=model.predict(x_test)
    predict_class=np.argmax(predict,axis=1)
    print(f'predict:{predict}')
    print(f'預測:{predict_class}')
    
'''展示端'''
#設定背景
img=np.full(shape=(28,28,1),fill_value=0,dtype=np.uint8)#0是黑，255是白
#初始化視窗
cv2.namedWindow('image')#視窗名稱是image
drawing=False #判斷是否按下右鍵時移動滑鼠
def draw_circle(event,x,y,flags,param):
    global img,drawing #取得全域變數
    if event == cv2.EVENT_LBUTTONDOWN: #右鍵被按下
        drawing=True
        cv2.circle(img=img,center=(x,y),radius=1,color=255,thickness=-1)
    if event == cv2.EVENT_MOUSEMOVE: #移動按鍵
        if drawing == True:
            cv2.circle(img=img,center=(x,y),radius=1,color=255,thickness=-1)
    if event == cv2.EVENT_LBUTTONUP: #右鍵放開
        drawing=False
        cv2.circle(img=img,center=(x,y),radius=1,color=255,thickness=-1)
cv2.setMouseCallback('image',draw_circle) #定義滑鼠動作
while True:
    cv2.imshow('image',img)
    key=cv2.waitKey(1)&0xFF
    if key == ord('s'):
        CNN()
        answer=input('amser')
        model.fit(img.reshape(1,28,28,1),tf.keras.utils.to_categorical(answer,num_classes=10),epochs=20,batch_size=128,verbose=1)
    elif key == ord('c'):
        img=np.full(shape=(28,28,1),fill_value=0,dtype=np.uint8)
    elif key == 27: #判斷是否按下Esc
        break
cv2.destroyWindow()
