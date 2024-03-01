import cv2
import numpy as np
img=cv2.imread('picture1.jpg')
img[0][0]=[0,0,255]#把0,0位置的顏色改成紅色
img[10:20,10:20]=[0,255,0] #10,10到20,20 變成綠色
cv2.imshow('image',img)#標題是image,圖片是img
cv2.waitKey(0)#停止，直到按下任意按鍵
cv2.destroyAllWindows()