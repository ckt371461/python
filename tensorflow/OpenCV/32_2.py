#使用webcam攝影機
import cv2
import numpy as np
cap=cv2.VideoCapture(0)# 0 表示使用第一个摄像头（通常是内置的摄像头）
while True:
    ret,frame=cap.read()#使用 cap.read() 函数读取视频帧。这个函数会返回一个布尔值（表示是否成功读取到了视频帧）和当前帧的图像数据。
    cv2.imshow('image',frame)
    if (cv2.waitKey(1)&0xFF) ==ord('q'): #等一秒且按下q離開
        break
'''0xFF 是十六进制数，它的十进制值是 255。在这段代码中，& 0xFF 操作的目的是将一个整数值强制转换为 8 位无符号整数（unsigned char）。
在 C/C++ 中，可以使用 & 0xFF 操作来将一个整数值的低 8 位保留下来，而把高位置零。比如：
int x = 0x12345678;
unsigned char low = x & 0xFF;  // low 的值为 0x78
这个操作在这段代码中被用来保证 cv2.waitKey() 函数只返回 8 位无符号整数，从而方便后面使用 ord() 函数来比较返回值是否等于 'q' 的 ASCII 码。'''
cap.release()
cv2.destroyAllWindows()