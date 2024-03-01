import matplotlib.pyplot as plt
t=[1,2,3,4]

plt.subplot(3,1,1,facecolor='y')#facecolor 可以決定背景顏色
plt.plot(t,[1,1,1,1],'rp')

plt.subplot(323,facecolor='k')#連在一起或分開(用逗號)都可以
plt.plot(t,t,'b>')

plt.subplot(3,2,4,facecolor='k')
plt.plot(t,[2,4,6,8],'bv')

plt.subplot(3,3,7,facecolor='b')
plt.plot(t,[1,4,9,16],'g^')

plt.subplot(3,3,8,facecolor='b')
plt.plot(t,[1,8,27,64],'g<')

plt.subplot(3,3,9,facecolor='b')
plt.plot(t,[1,8,27,64],'gd')

plt.show()