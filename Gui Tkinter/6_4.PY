import tkinter as tk
import tkinter.messagebox as mb
def hello():
    mb.showinfo('this is showinfo','showinfo')
    mb.showwarning('this is showwarning','showwarning')
    mb.showerror('this is showerror','showerror')
    mb.askokcancel('this is askokcancel','askokcancel')
    mb.askyesno('this is askyesno','askyesno')
    mb.askquestion('this is askquestion','askquestion')
    '''result=mb.askquestion('this is askquestion','askquestion')
    print(result)'''#這樣也可
    mb.askretrycancel('this is askretrycancel','askretrycancel')
    mb.askyesnocancel('this is askyesnocancel','askyesnocancel')



window=tk.Tk()
button=tk.Button(window,text='say hello',command=hello)
button.pack()
window.mainloop()