#製作手寫版
import cv2
import numpy as np
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
    if key == ord('c'):
        img=np.full(shape=(28,28,1),fill_value=0,dtype=np.uint8)
    elif key == 27: #判斷是否按下Esc
        break
cv2.destroyWindow()