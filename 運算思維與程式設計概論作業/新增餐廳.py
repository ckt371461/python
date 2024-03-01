import tkinter as tk

# 創建主窗口
root = tk.Tk()
root.title("新增餐廳")

newrestaurant = tk.Label(root, text="名稱")
newrestaurant.pack(pady=5)
restaurantname = tk.Entry(root)
restaurantname.pack(pady=5)

label_low = tk.Label(root, text="價格下限:")
label_low.pack(pady=5)
price_low = tk.Entry(root)
price_low.pack(pady=5)

label_high = tk.Label(root, text="價格上限:")
label_high.pack(pady=5)
price_high = tk.Entry(root)
price_high.pack(pady=5)

type_label = tk.Label(root, text="類別")
type_label.pack(pady=5)

listbox_type = tk.Listbox(root, selectmode=tk.MULTIPLE)
listbox_type.pack(pady=10)
types = ["飯類", "麵類", "堡類", "餃類"]
for item in types:
    listbox_type.insert(tk.END, item)

specialty_label = tk.Label(root, text="特性")
specialty_label.pack(pady=5)

listbox_specialty = tk.Listbox(root, selectmode=tk.MULTIPLE)
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

button = tk.Button(root, text="完成", command=button_clicked)
button.pack()

# 啟動主事件迴圈
root.mainloop()