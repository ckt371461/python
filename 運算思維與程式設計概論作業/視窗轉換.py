
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
        tk.Label(self, text="午餐吃甚麼").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="開始",
                  command=lambda: master.switch_frame(budgete)).pack()
        tk.Button(self, text="隨機",
                  command=lambda: master.switch_frame(rd)).pack()
        tk.Button(self, text="新增餐廳",
                  command=lambda: master.switch_frame(new)).pack()

class budgete(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        def button_clicked():
            price = price_entry.get()
            return price
        tk.label = tk.Label(self, text="預算:")
        tk.label.pack(pady=5)
        price_entry = tk.Entry(self)
        price_entry.pack(pady=5)
        tk.button = tk.Button(self, text="下一步", command=lambda: (button_clicked(), master.switch_frame(type)))
        tk.button.pack()
        tk.Button(self, text="回選單",
                  command=lambda: master.switch_frame(StartPage)).pack()
class type(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        def button_clicked():
            selected_indices = tk.listbox.curselection()
            selected_items = [tk.listbox.get(idx) for idx in selected_indices]
            return selected_items
        tk.label = tk.Label(self, text="請選擇食物種類:")
        tk.label.pack(pady=5)
        tk.listbox = tk.Listbox(self, selectmode=tk.MULTIPLE)  # 選擇多個選項，使用 tk.MULTIPLE
        tk.listbox.pack(pady=10)
        
        items = ["飯類", "麵類", "堡類", "餃類"]
        for item in items:
            tk.listbox.insert(tk.END, item)
        tk.button = tk.Button(self, text="下一步", command=lambda: (button_clicked(), master.switch_frame(like))).pack()
        tk.Button(self, text="回選單",
                  command=lambda: master.switch_frame(StartPage)).pack()
class like(tk.Frame):
     def __init__(self, master):
         tk.Frame.__init__(self, master)
         def button_clicked():
             selected_indices = tk.listbox.curselection()
             selected_items = [tk.listbox.get(idx) for idx in selected_indices]
             return selected_items
         tk.label = tk.Label(self, text="請選擇偏好:")
         tk.label.pack(pady=5)
         tk.listbox = tk.Listbox(self, selectmode=tk.MULTIPLE)  # 選擇多個選項，使用 tk.MULTIPLE
         tk.listbox.pack(pady=10)
         items = ["偏好1", "偏好2"]
         for item in items:
             tk.listbox.insert(tk.END, item)
         tk.button = tk.Button(self, text="下一步", command=lambda: (button_clicked(), master.switch_frame(dislike))).pack()
         tk.Button(self, text="回選單",
                   command=lambda: master.switch_frame(StartPage)).pack()
class dislike(tk.Frame):
     def __init__(self, master):
         tk.Frame.__init__(self, master)
         def button_clicked():
             selected_indices = tk.listbox.curselection()
             selected_items = [tk.listbox.get(idx) for idx in selected_indices]
             return selected_items
         tk.label = tk.Label(self, text="請選擇忌口:")
         tk.label.pack(pady=5)
         tk.listbox = tk.Listbox(self, selectmode=tk.MULTIPLE)  # 選擇多個選項，使用 tk.MULTIPLE
         tk.listbox.pack(pady=10)
         items = ["辣", "香菜"]
         for item in items:
             tk.listbox.insert(tk.END, item)
         tk.button = tk.Button(self, text="看結果", command=lambda: (button_clicked(), master.switch_frame(choose))).pack()
         tk.Button(self, text="回選單",
                   command=lambda: master.switch_frame(StartPage)).pack()
class choose(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title("午餐吃甚麼")

        # 創建 Text 小部件
        self.text_widget = scrolledtext.ScrolledText(self, wrap=tk.WORD)
        self.text_widget.pack(expand=True, fill=tk.BOTH)

        # 將 DataFrame 轉換為字串並顯示在 Text 小部件中
        dataframe_str = str(result)  # 使用你的 result 字典
        self.text_widget.insert(tk.END, dataframe_str)

        # 創建兩個按鈕
        button1 = tk.Button(self, text="退出", command=self.button1_clicked)
        button1.pack(side=tk.LEFT, padx=10)

        button2 = tk.Button(self, text="隨機選擇", command=self.button2_clicked)
        button2.pack(side=tk.LEFT, padx=10)
        tk.Button(self, text="回選單",
                  command=lambda: master.switch_frame(StartPage)).pack()

    def button1_clicked(self):
        print("按鈕1被點擊！")

    def button2_clicked(self):
        print("按鈕2被點擊！")

# 創建字典
result = {'名稱': 'new', '價格下限': 50, '飯類': 1, '麵類': 0, '堡類': 1, '辣': 1, '香菜': 1}
class rd(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title("午餐吃甚麼")

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
        tk.Button(self, text="回選單",
                  command=lambda: master.switch_frame(StartPage)).pack()

    def button1_clicked(self):
        print("按鈕1被點擊！")

    def button2_clicked(self):
        print("按鈕2被點擊！")

# 創建字典
result = {'名稱': 'new', '價格下限': 50, '飯類': 1, '麵類': 0, '堡類': 1, '辣': 1, '香菜': 1}

class new(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        newrestaurant = tk.Label(self, text="名稱")
        newrestaurant.pack(pady=5)
        restaurantname = tk.Entry(self)
        restaurantname.pack(pady=5)
        
        label_low = tk.Label(self, text="價格下限:")
        label_low.pack(pady=5)
        price_low = tk.Entry(self)
        price_low.pack(pady=5)
        
        label_high = tk.Label(self, text="價格上限:")
        label_high.pack(pady=5)
        price_high = tk.Entry(self)
        price_high.pack(pady=5)
        
        type_label = tk.Label(self, text="類別")
        type_label.pack(pady=5)
        
        listbox_type = tk.Listbox(self, selectmode=tk.MULTIPLE)
        listbox_type.pack(pady=10)
        types = ["飯類", "麵類", "堡類", "餃類"]
        for item in types:
            listbox_type.insert(tk.END, item)
        
        specialty_label = tk.Label(self, text="特性")
        specialty_label.pack(pady=5)
        
        listbox_specialty = tk.Listbox(self, selectmode=tk.MULTIPLE)
        listbox_specialty.pack(pady=10)
        like_eat_items = ["辣", "香菜"]
        for item in like_eat_items:
            listbox_specialty.insert(tk.END, item)
        
        def button_clicked():
            selected_type_indices = listbox_type.curselection()
            selected_types = [listbox_type.get(idx) for idx in selected_type_indices]
        
            selected_specialty_indices = listbox_specialty.curselection()
            selected_specialty = [listbox_specialty.get(idx) for idx in selected_specialty_indices]
        
            # 將類別和特性的內容作為 result_dict 的鍵，並將包含在內的數值設為1，不包含的數值設為0
            type_dict = {item: 1 if item in selected_types else 0 for item in types}
            specialty_dict = {item: 1 if item in selected_specialty else 0 for item in like_eat_items}
        
            # 將 "名稱"、"價格下限" 和 "價格上限" 加入 result_dict
            result_dict = {
                "名稱": restaurantname.get(),
                "價格下限": int(price_low.get()),
                "價格上限": int(price_high.get()),
            }
        
            # 將 "類別" 和 "特性" 的內容合併到 result_dict 中
            result_dict.update(type_dict)
            result_dict.update(specialty_dict)
        
            print(result_dict)
            #write_to_excel(result_dict)
        
        button = tk.Button(self, text="完成", command=lambda: (button_clicked(),master.switch_frame(complete)))
        button.pack()
        tk.Button(self, text="回選單",
                  command=lambda: master.switch_frame(StartPage)).pack()
class complete(tk.Frame):
     def __init__(self, master):
         tk.Frame.__init__(self, master)
         tk.label = tk.Label(self, text="新增完成")
         tk.label.pack(pady=5)
         tk.Button(self, text="回選單",
                   command=lambda: master.switch_frame(StartPage)).pack()

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()