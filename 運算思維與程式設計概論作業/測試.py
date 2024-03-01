import tkinter as tk
from tkinter import scrolledtext

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="This is the start page").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Open page one",
                  command=lambda: master.switch_frame(PageOne)).pack()
        tk.Button(self, text="Open page two",
                  command=lambda: master.switch_frame(PageTwo)).pack()
        tk.Button(self, text="Open DataFrame Viewer",
                  command=lambda: master.switch_frame(DataFrameViewerApp)).pack()

class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="This is page one").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Return to start page",
                  command=lambda: master.switch_frame(StartPage)).pack()

class PageTwo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="This is page two").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Return to start page",
                  command=lambda: master.switch_frame(StartPage)).pack()

class DataFrameViewerApp(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title("DataFrame Viewer")

        # 創建 Text 小部件
        self.text_widget = scrolledtext.ScrolledText(self, wrap=tk.WORD)
        self.text_widget.pack(expand=True, fill=tk.BOTH)

        # 將 DataFrame 轉換為字串並顯示在 Text 小部件中
        dataframe_str = str(result)  # 使用你的 result 字典
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

if __name__ == "__main__":
    app = SampleApp()
    app.geometry("400x300")  # 設置主窗口大小
    app.mainloop()