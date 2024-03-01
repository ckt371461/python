import matplotlib.pyplot as plt
x=[1,2,3,4]
y=[1,4,9,16]
plt.plot(x,y,'ro')#第一個字母表示顏色，第二個是形狀
#顏色:  藍b,綠g,紅r,青c,粉紅m,黃y,黑k,白w
plt.axis([0,6,0,20])#圖表範圍x從0-6,y從0-20
plt.show()