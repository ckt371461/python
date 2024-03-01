import tkinter as tk
window=tk.Tk()
window.wm_title('Window')
window.maxsize(width=800,height=600) #按右上角的放大鍵
window.minsize(width=500,height=300) #預設
#window.resizable(width=True,height=False) #決定能不能放大縮小，不能得連右上角的視窗都沒用(maxsize沒意義)
label1=tk.Label(window,text='Hello World!')
label1.pack()
#pack() 和 place()的差別在於pack是按順序給位置而place 是指定位置給他
label2=tk.Label(window,text='Hello World!',anchor='e',bg='light green',font=('times new roman',30),fg='dark blue',height=10,width=10)
label2.place(x=10,y=30)
window.mainloop()