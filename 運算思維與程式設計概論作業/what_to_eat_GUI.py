import pandas as pd
import tkinter as tk
from tkinter import scrolledtext

data = pd.read_excel("restaurant.xlsx")


def sieve(budget, categories, prefer, abstain):
    # 將 StringVar 轉換為列表
    categories = categories.replace("(", "").replace(")", "").replace("'", "")
    categories_list = [category.strip() for category in categories.split(',') if category]

    prefer = prefer.replace("(", "").replace(")", "").replace("'", "")
    likes_list = [like.strip() for like in prefer.split(',') if like]
    
    abstain = abstain.replace("(", "").replace(")", "").replace("'", "")
    dislikes_list = [dislike.strip() for dislike in abstain.split(',') if dislike]
    
    # 複製一份 DataFrame，以免修改原始數據
    outcome = data.copy()
    
    # 預算篩選
    outcome = outcome[(outcome['價格下限'] <= budget) & (outcome['價格上限'] >= budget)]
    
    # 類別篩選
    if categories_list:
        category_condition = outcome[categories_list].any(axis=1)
        outcome = outcome[category_condition]
    
    # 喜好和忌口篩選
    for item in likes_list:
        outcome = outcome[outcome[item] == 1]
    
    for item in dislikes_list:
        outcome = outcome[outcome[item] == 0]

    return outcome


def write_to_excel(new_data):
    global data
    if '名稱' in data.columns and data['名稱'].isin([new_data['名稱']]).any():
        print(f"名稱 {new_data['名稱']} 已存在，不進行寫入。")
        return
    new_row = pd.DataFrame([new_data], columns=data.columns)
    data = pd.concat([data, new_row], ignore_index=True)
    data.to_excel("restaurant.xlsx", index=False)
    print(f"名稱 {new_data['名稱']} 成功寫入 'restaurant.xlsx'")


def random(dataframe):#隨機輸出一筆資料
    return dataframe.sample(n=1)




#GUI
class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.shared_data = {
            '預算': tk.IntVar(),
            '類別': tk.StringVar(),
            '偏好': tk.StringVar(),
            '忌口': tk.StringVar(),
        }
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self, self.shared_data)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class StartPage(tk.Frame):
    def __init__(self, master, shared_data):
        tk.Frame.__init__(self, master)
        self.shared_data = shared_data
        tk.Label(self, text="午餐吃甚麼").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="開始", command=lambda: master.switch_frame(budgete)).pack()
        tk.Button(self, text="隨機", command=lambda: master.switch_frame(randomchoose)).pack()
        tk.Button(self, text="新增餐廳", command=lambda: master.switch_frame(new_1)).pack()


class budgete(tk.Frame):
    def __init__(self, master, shared_data):
        tk.Frame.__init__(self, master)
        self.shared_data = shared_data
        def button_clicked():
            price = int(price_entry.get())
            self.shared_data['預算'].set(price)
        tk.Label(self, text="預算:").pack(pady=5)
        price_entry = tk.Entry(self)
        price_entry.pack(pady=5)
        tk.Button(self, text="下一步", command=lambda: (button_clicked(), master.switch_frame(type))).pack()
        tk.Button(self, text="回選單", command=lambda: master.switch_frame(StartPage)).pack()

class type(tk.Frame):
    def __init__(self, master, shared_data):
        tk.Frame.__init__(self, master)
        self.shared_data = shared_data
        def button_clicked():
            selected_indices = tk.listbox.curselection()
            selected_items = [tk.listbox.get(idx) for idx in selected_indices]
            self.shared_data['類別'].set(selected_items)
        tk.Label(self, text="請選擇食物種類:").pack(pady=5)
        tk.listbox = tk.Listbox(self, selectmode=tk.MULTIPLE)  
        tk.listbox.pack(pady=10)
        items = ["飯類", "麵類", "堡類", "餃類"]
        for item in items:
            tk.listbox.insert(tk.END, item)
        tk.Button(self, text="下一步", command=lambda: (button_clicked(), master.switch_frame(like))).pack()
        tk.Button(self, text="回選單", command=lambda: master.switch_frame(StartPage)).pack()

class like(tk.Frame):
    def __init__(self, master, shared_data):
        tk.Frame.__init__(self, master)
        self.shared_data = shared_data
        def button_clicked():
            selected_indices = tk.listbox.curselection()
            selected_items = [tk.listbox.get(idx) for idx in selected_indices]
            self.shared_data['偏好'].set(selected_items)
        tk.Label(self, text="請選擇偏好:").pack(pady=5)
        tk.listbox = tk.Listbox(self, selectmode=tk.MULTIPLE)
        tk.listbox.pack(pady=10)
        items = ["辣", "香菜"]
        for item in items:
            tk.listbox.insert(tk.END, item)
        tk.Button(self, text="下一步", command=lambda: (button_clicked(), master.switch_frame(dislike))).pack()
        tk.Button(self, text="回選單", command=lambda: master.switch_frame(StartPage)).pack()

class dislike(tk.Frame):
    def __init__(self, master, shared_data):
        tk.Frame.__init__(self, master)
        self.shared_data = shared_data
        def button_clicked():
            selected_indices = tk.listbox.curselection()
            selected_items = [tk.listbox.get(idx) for idx in selected_indices]
            self.shared_data['忌口'].set(selected_items)
        tk.Label(self, text="請選擇忌口:").pack(pady=5)
        tk.listbox = tk.Listbox(self, selectmode=tk.MULTIPLE)
        tk.listbox.pack(pady=10)
        items = ["辣", "香菜"]
        for item in items:
            tk.listbox.insert(tk.END, item)
        tk.Button(self, text="看結果", command=lambda: (button_clicked(), master.switch_frame(choose))).pack()
        tk.Button(self, text="回選單", command=lambda: master.switch_frame(StartPage)).pack()

class choose(tk.Frame):
    def __init__(self, master, shared_data):
        tk.Frame.__init__(self, master)
        self.shared_data = shared_data
        master.title("午餐吃甚麼")
        self.text_widget = scrolledtext.ScrolledText(self, wrap=tk.WORD)
        self.text_widget.pack(expand=True, fill=tk.BOTH)
        dataframe = sieve(self.shared_data['預算'].get(),self.shared_data['類別'].get(),self.shared_data['偏好'].get(),self.shared_data['忌口'].get())
        self.text_widget.insert(tk.END, dataframe)
        tk.Button(self, text="隨機選擇", command=lambda: (button_clicked(),master.switch_frame(rd))).pack()
        tk.Button(self, text="回選單", command=lambda: master.switch_frame(StartPage)).pack()
        def button_clicked():
            global final_outcome
            final_outcome = dataframe
class rd(tk.Frame):
    def __init__(self, master, shared_data):
        tk.Frame.__init__(self, master)
        self.shared_data = shared_data
        master.title("午餐吃甚麼")

        # 創建 Text 小部件
        self.text_widget = scrolledtext.ScrolledText(self, wrap=tk.WORD)
        self.text_widget.pack(expand=True, fill=tk.BOTH)

        # 將 DataFrame 轉換為字串並顯示在 Text 小部件中
        dataframe_str = str(random(final_outcome))  # 使用你的 result 字典
        self.text_widget.insert(tk.END, dataframe_str)

        tk.Button(self, text="再次隨機", command=lambda: master.switch_frame(rd)).pack()
        tk.Button(self, text="回選單",
                  command=lambda: master.switch_frame(StartPage)).pack()

class randomchoose(tk.Frame):
    def __init__(self, master, shared_data):
        tk.Frame.__init__(self, master)
        self.shared_data = shared_data
        master.title("午餐吃甚麼")

        # 創建 Text 小部件
        self.text_widget = scrolledtext.ScrolledText(self, wrap=tk.WORD)
        self.text_widget.pack(expand=True, fill=tk.BOTH)

        # 將 DataFrame 轉換為字串並顯示在 Text 小部件中
        dataframe_str = str(random(data))  # 使用你的 result 字典
        self.text_widget.insert(tk.END, dataframe_str)

        tk.Button(self, text="再次隨機", command=lambda: master.switch_frame(randomchoose)).pack()
        tk.Button(self, text="回選單",
                  command=lambda: master.switch_frame(StartPage)).pack()
            


class new_1(tk.Frame):
    def __init__(self, master, shared_data):
        tk.Frame.__init__(self, master)
        self.shared_data = shared_data
        newrestaurant = tk.Label(self, text="名稱")
        newrestaurant.pack(pady=5)
        self.restaurantname = tk.Entry(self)
        self.restaurantname.pack(pady=5)

        type_label = tk.Label(self, text="類別")
        type_label.pack(pady=5)

        self.listbox_type = tk.Listbox(self, selectmode=tk.MULTIPLE)
        self.listbox_type.pack(pady=10)
        types = ["飯類", "麵類", "堡類", "餃類"]
        for item in types:
            self.listbox_type.insert(tk.END, item)

        def button_clicked():
            selected_type_indices = self.listbox_type.curselection()
            selected_types = [self.listbox_type.get(idx) for idx in selected_type_indices]

            # 將類別和特性的內容作為 shared_data 的鍵，並將包含在內的數值設為1，不包含的數值設為0
            type_dict = {item: 1 if item in selected_types else 0 for item in types}

            # 將 "名稱"、"類別" 的內容合併到 shared_data 中
            self.shared_data.update({
                "名稱": self.restaurantname.get(),
            })
            self.shared_data.update(type_dict)

        button = tk.Button(self, text="下一步", command=lambda: (button_clicked(), master.switch_frame(new_2)))
        button.pack()
        tk.Button(self, text="回選單", command=lambda: master.switch_frame(StartPage)).pack()

class new_2(tk.Frame):
    def __init__(self, master, shared_data):
        tk.Frame.__init__(self, master)
        self.shared_data = shared_data

        label_low = tk.Label(self, text="價格下限:")
        label_low.pack(pady=5)
        price_low = tk.Entry(self)
        price_low.pack(pady=5)

        label_high = tk.Label(self, text="價格上限:")
        label_high.pack(pady=5)
        price_high = tk.Entry(self)
        price_high.pack(pady=5)

        specialty_label = tk.Label(self, text="特性")
        specialty_label.pack(pady=5)

        listbox_specialty = tk.Listbox(self, selectmode=tk.MULTIPLE)
        listbox_specialty.pack(pady=10)
        like_eat_items = ["辣", "香菜"]
        for item in like_eat_items:
            listbox_specialty.insert(tk.END, item)

        def button_clicked():
            selected_specialty_indices = listbox_specialty.curselection()
            selected_specialty = [listbox_specialty.get(idx) for idx in selected_specialty_indices]
            specialty_dict = {item: 1 if item in selected_specialty else 0 for item in like_eat_items}

            # 將 "價格下限" 和 "價格上限" 加入 shared_data
            self.shared_data.update({
                "價格下限": int(price_low.get()),
                "價格上限": int(price_high.get()),
            })

            self.shared_data.update(specialty_dict)

            write_to_excel(self.shared_data)

        button = tk.Button(self, text="完成", command=lambda: (button_clicked(), master.switch_frame(complete)))
        button.pack()
        tk.Button(self, text="回選單", command=lambda: master.switch_frame(StartPage)).pack()

class complete(tk.Frame):
    def __init__(self, master,shared_data):
         tk.Frame.__init__(self, master)
         tk.label = tk.Label(self, text="新增完成")
         tk.label.pack(pady=5)
         tk.Button(self, text="回選單", command=lambda: master.switch_frame(StartPage)).pack()

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()