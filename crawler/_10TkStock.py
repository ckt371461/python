from tkinter import ttk
import tkinter as tk
import sqlite3

def View():
    for item in tree.get_children():
        tree.delete(item)
    con1 = sqlite3.connect("stockPrice.db")
    cur1 = con1.cursor()
    cmd = sqltext.get(1.0, "end-1c")
    #The first part, "1.0" means that the input should be read from line one, character zero (ie: the very first character).
    # END is an imported constant which is set to the string "end". The END part means to read until the end of the text box is reached.
    # The only issue with this is that it actually adds a newline to our input. So, in order to fix it we should change END to end-1c
    # The -1c deletes 1 character, while -2c would mean delete two characters, and so on. 
    cur1.execute(cmd)
    rows = cur1.fetchall()
    for row in rows:
        # print(row) 
        tree.insert("", tk.END, values=row)        
    con1.close()

root = tk.Tk()

sqltext = tk.Text(root, height=3, width=100)
sqltext.pack()
sqltext.insert(tk.END, "SELECT * FROM stockPrice WHERE 收盤價 > 410 ORDER BY 收盤價 DESC")

buttonQuery = tk.Button(text="查詢", command=View)
buttonQuery.pack(pady=10)

tree = ttk.Treeview(root, column=("c1", "c2", "c3", "c4"), show='headings')
tree.column("#1", anchor=tk.CENTER)
tree.heading("#1", text="日期")
tree.column("#2", anchor=tk.CENTER)
tree.heading("#2", text="開盤")
tree.column("#3", anchor=tk.CENTER)
tree.heading("#3", text="收盤價")
tree.column("#4", anchor=tk.CENTER)
tree.heading("#4", text="成交筆數")
tree.pack()

root.mainloop()
