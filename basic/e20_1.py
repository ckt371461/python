import matplotlib.pyplot as plt
plt.figure()
x=(0,3,6,9,14)
y=(0,5,2,8,10)

plt.subplot(2,2,1)
# 把整個figur分成兩行兩列，在左上角第一個位置我要plot上一個圖
plt.scatter(x,y)

plt.subplot(2,2,2)
plt.plot(x,y)

plt.subplot(2,1,2)
plt.plot(x,y,'-o')
plt.show()