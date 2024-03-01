from tkinter import ttk
#Treeview 组件是 ttk 模块的组件之一，它既可以作为树结构使用，也可以作为表格展示数据（tkinter 并没有表格控件）。
import tkinter as tk
import sqlite3

root = tk.Tk()

textSql = tk.Text(root, height=3, width=100)
textSql.pack()
textSql.insert(tk.END, "SELECT * FROM stockPrice")

button1 = tk.Button(text="查詢")
button1.pack(pady=10)#pady定義物件外的空隙大小

tree = ttk.Treeview(root, column=("c1", "c2", "c3", "c4"), show='headings')
#创建 Treeview 使用 ttk.Treeview 类
# ex: tree = ttk.Treeview(master,options)
# columns	接收一个列表（tuple），列表中的每个元素都代表表格中的一列（可以理解为 ID），列表的长度就是表格的列数
# show	有 "tree"、"headings"、"tree headings" 三种选项，分别代表显示图标列（编号为 "#0"）、不显示图标列（仅显示数值列）以及显示所有列（图标列和数值列）。 
# https://blog.csdn.net/weixin_43302112/article/details/122172171
tree.heading("#1", text="日期",anchor=tk.CENTER)#方法一
tree.column("#2", anchor=tk.CENTER)#方法二(分兩行)
tree.heading("#2", text="開盤")
tree.column("#3", anchor=tk.CENTER)
tree.heading("#3", text="收盤價")
tree.column("#4", anchor=tk.CENTER)
tree.heading("#4", text="成交筆數")
item = [1,1,1,1]
tree.insert("",tk.END,values=item)
tree.pack()

root.mainloop()
