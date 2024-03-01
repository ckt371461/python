import tkinter as tk

def start():
    print("Button start clicked!")
def random():
    print("Button random clicked!")
def new():
    print("Button new clicked!")

# 建立主視窗
root = tk.Tk()
root.title("午餐吃甚麼")

# 創建三個按鈕並設定點擊時的動作
button1 = tk.Button(root, text="開始", command=start)
button2 = tk.Button(root, text="隨機選擇", command=random)
button3 = tk.Button(root, text="新增餐廳", command=new)

# 將按鈕放置在主視窗中
button1.pack(pady=10)
button2.pack(pady=10)
button3.pack(pady=10)

# 啟動主迴圈
root.mainloop()