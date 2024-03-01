import tkinter as tk
from PIL import Image,ImageTk
window=tk.Tk()
c1=tk.Canvas(window,height=200,width=1000)
arc=c1.create_arc((10,10,100,100),start=0,extent=200,fill='red',outline='green')#畫弧(arc)
img=ImageTk.PhotoImage(Image.open('picture.png').resize((200,100)))
c1.create_image(300,100,image=img)
c1.create_line(500,100,600,10)#從(500,100)到(600,10)
c1.create_text(700,50,text='hello world')
c1.create_rectangle(800,50,900,100,fill='yellow')
def paint(event):
    x1,y1=(event.x-1),(event.y-1)
    x2,y2=(event.x+1),(event.y+1)
    c1.create_oval(x1,y1,x2,y2,fill='black')
c1.bind('<B1-Motion>',paint)#綁定滑鼠
#c1.bind('<Button-1>',paint)#綁定滑鼠左鍵
'''
<KeyPress-A>表示A键被按下,其中的A可以换成其他的键位

<Control-V>表示按下的是Ctrl和V键,V可以换成其他键位

<F1>表示按下的是F1键,对于Fn系列的,都可以随便换'''

c1.pack()

#第一個元祖是決定大小，這裡是從(10,10)到(100,100)
window.mainloop()