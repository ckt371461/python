import numpy as np
import matplotlib.pyplot as plt
plt.plot([1,2,3,4],[0,0.3,0.6,0.9],'gx')
plt.plot([1,2,3,4],[0,0.3,0.6,0.9],'r--')

#加入誤差值delta
x=1+np.arange(30)/10 #np.arange(n) 會產生相差為1的n組資料
delta=np.random.uniform(low=-0.1,high=0.1,size=(30,)) #產生-0.1-0.1之間的30組資料在元組中
y=0.3*x-0.3+delta

plt.plot(x,y,'bo')
plt.ylabel('y')
plt.xlabel('x')
plt.show()

#計算殘差
sum1=0.0
i=0
for x1 in x:
    y1=0.3*x1-0.3
    y2=0.3*x1-0.3+delta[i]
    #abs() 函数返回数字的绝对值。
    sum1=sum1+abs(y1-y2)
    i+=1
print('殘差=',sum1/30)