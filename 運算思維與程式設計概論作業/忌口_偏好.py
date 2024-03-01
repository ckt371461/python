import tkinter as tk
root = tk.Tk()

listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)  # 選擇多個選項，使用 tk.MULTIPLE
listbox.pack(pady=10)#pack(pady=10) 中的 pady 是一個參數，用來設置在垂直方向上的外部填充
#（padding）。這表示在 Listbox 小部件的上方和下方都會有 10 像素的空間，用於增加小部件的邊界。


items = ["辣", "香菜"]
for item in items:
    listbox.insert(tk.END, item)

def button_clicked():
    selected_indices = listbox.curselection()
    selected_items = [listbox.get(idx) for idx in selected_indices]
    return selected_items

button = tk.Button(root, text="下一步", command=button_clicked)
button.pack()

root.mainloop()