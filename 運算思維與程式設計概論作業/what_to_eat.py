import pandas as pd
import tkinter as tk


data = pd.read_excel("restaurant.xlsx")


def sieve(budget, categories=[], abstain=[],prefer=[]):#篩選合適餐廳
    outcome = data[(data['價格下限'] <= budget) & (data['價格上限'] >= budget)]
    category_condition = outcome[categories].any(axis=1)
    outcome = outcome[category_condition]
    for item in abstain:
        outcome = outcome[outcome[item] == 0]
    for item in prefer:
        outcome = outcome[outcome[item] == 1]
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


new_data = {'名稱': 'new', '價格下限': 50, '飯類': 1, '麵類': 0, '堡類': 1, '辣': 1, '香菜': 1}
write_to_excel(new_data)

result = sieve(90, ['堡類', '飯類'], ['香菜'])
print(result)
print(random(result))

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

app = DataFrameViewerApp(result)
app.geometry("400x300")
app.mainloop()