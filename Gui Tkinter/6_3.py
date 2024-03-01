import tkinter as tk
from PIL import Image,ImageTk
window=tk.Tk()
img1=Image.open('picture.png')
#img1.thumbnail((20,20))#這裡不用用等式指定
img1=img1.resize((200,200)) #這裡要用等式指定
img1.show()
img_1=ImageTk.PhotoImage(image=img1)
def event1():
    print('btnl pressed')
but1=tk.Button(window,text='press me',image=img_1,command=event1)
but1.pack()
window.mainloop()