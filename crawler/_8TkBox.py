import tkinter as tk
window = tk.Tk() 
T = tk.Text(window, height=2, width=30)
T.pack()
T.insert(tk.END, "SELECT * FROM stockPrice")#T.insert(tk.INSERT, "SELECT * FROM stockPrice")
window.mainloop()
