import tkinter as tk
window=tk.Tk()
entry1=tk.Entry(window)
entry1.pack()
def event1():
    print(entry1.get())
    v.set(entry1.get())
button1=tk.Button(window,text='hello',command=event1)
button1.pack()
v=tk.StringVar()
label1=tk.Label(window,textvariable=v)
label1.pack()
v.set('enter some string')
window.mainloop()