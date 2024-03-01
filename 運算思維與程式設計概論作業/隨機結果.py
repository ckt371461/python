import tkinter as tk
from tkinter import scrolledtext
import pandas as pd

class DataFrameViewerApp(tk.Tk):
    def __init__(self, dataframe):
        tk.Tk.__init__(self)
        self.title("結果")

        # 創建 Text 小部件
        self.text_widget = scrolledtext.ScrolledText(self, wrap=tk.WORD)
        self.text_widget.pack(expand=True, fill=tk.BOTH)

        # 將 DataFrame 轉換為字串並顯示在 Text 小部件中
        dataframe_str = str(dataframe)
        self.text_widget.insert(tk.END, dataframe_str)

        # 創建兩個按鈕
        button1 = tk.Button(self, text="退出", command=self.button1_clicked)
        button1.pack(side=tk.LEFT, padx=10)

        button2 = tk.Button(self, text="再次隨機", command=self.button2_clicked)
        button2.pack(side=tk.LEFT, padx=10)

    def button1_clicked(self):
        print("按鈕1被點擊！")

    def button2_clicked(self):
        print("按鈕2被點擊！")

# 創建字典
result = {'名稱': 'new', '價格下限': 50, '飯類': 1, '麵類': 0, '堡類': 1, '辣': 1, '香菜': 1}

# 創建視窗並顯示 DataFrame 內容
#這邊到時侯要加上random函數在result前
app = DataFrameViewerApp(result)
app.mainloop()