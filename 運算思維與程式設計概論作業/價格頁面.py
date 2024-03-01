import tkinter as tk

def button_clicked():
    price = price_entry.get()
    return price

# 創建主窗口
root = tk.Tk()

label = tk.Label(root, text="預算:")
label.pack(pady=5)
price_entry = tk.Entry(root)
price_entry.pack(pady=5)

button = tk.Button(root, text="下一步", command=button_clicked)
button.pack()

# 啟動主事件迴圈
root.mainloop()
