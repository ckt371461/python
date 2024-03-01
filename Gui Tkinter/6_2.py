import tkinter as tk
window=tk.Tk()
from PIL import ImageTk,Image
img=Image.open('picture.png')
img_tk=ImageTk.PhotoImage(img) #用tk 打開的方法
label1=tk.Label(window,image=img_tk) 
label1.pack()
#img.show() 用本身的方式打開
window.mainloop() 

