#了解mnist的資料庫內容
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
#載入資料
(x_train,y_train),(x_test,y_test)=tf.keras.datasets.mnist.load_data() #載入mnist的手寫資料
#印出形狀
print(f'x_train_shape={x_train.shape}')#x_train_shape=(60000, 28, 28)
print(f'y_train_shape={y_train.shape}')#y_train_shape=(60000,)
#顯示資料
def printMatrix(matrix):
    for i in range(matrix.shape[0]):
        str1=''
        for j in range(matrix.shape[1]):
            str1+='%3.0f'%matrix[i][j]
        print(str1)
    print('')
printMatrix(x_train[0])
print(y_train[0])
#顯示圖形
num=0
plt.title(f'x_train[{num} Label:{y_train[num]}]')#顯示是哪筆資料和資料的答案
plt.imshow(x_train[num],cmap=plt.get_cmap('gray_r')) #顏色範圍選用灰階
plt.show()
#平行顯示圖形內容值,xy是值在矩陣中的位置，矩陣為[找到的數量,784]大小的矩陣
def display_mult_value(start,stop,label):
    image=[] #空陣列視為False
    num=start
    if num <= stop:
        while not image:
            if int(y_train[num]) == label:
                image=x_train[num].reshape([1,28*28]) #將資料轉為1維的資料
                break
            num=num+1
        for i in range(num+1,stop):
            if int(y_train[i]) == label:
                image=np.concatenate((image,x_train[i].reshape([1,28*28])))
                #image=np.vstack((image,x_train[i].reshape([1,28*28]))) #這個也可以，這個可以加不同大小的
        plt.imshow(image,cmap=plt.get_cmap('gray_r'))
        plt.show() 
display_mult_value(0,2000,1) 
display_mult_value(0,2000,8)      