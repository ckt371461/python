import matplotlib.pyplot as plt
import matplotlib.image as mpimg
t=[100,200,300,400]
plt.plot(t,t,'r--')
plt.xlabel('xlabel')
plt.ylabel('ylabel')
plt.title('title')
img=mpimg.imread('point_shape.jpg')
implot=plt.imshow(img)
plt.text(500,500,'hello world')
plt.savefig('my.png')
plt.show()