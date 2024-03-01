import tkinter as tk
window = tk.Tk() #記得加上括號，不然會出錯TypeError: Misc.mainloop() missing 1 required positional argument: 'self'
#步驟二、定義一個視窗 名叫 window
window.tittle = 'window' 
#步驟三、設定標題
window.geometry('600x300')
# #步驟四、設定像素大小
lbl_1 = tk.Label(window, text='Hello World', bg='yellow', fg='#123422', font=('Arial', 12))
#步驟五、宣告一個標籤
# bg是背景顏色，fg是文字顏色,font是字體種類及大小
lbl_1.grid(column=0, row=0)
#lbl_1.pack()
#步驟六、設定放置的位置 ( 使用 grid 佈局 )
'''
版面管理員 (Layout Manabger) 用來設定 GUI 應用程式中元件的擺放方式, 選擇適當的版面是GUI 程式首要的工作. Tkinter 透過三個方法提供了三種版面管理員 :
1.pack()
2.grid()
3.place()
pack() 為流水式排版, 預設元件會依加入先後順序由上而下, 由左而右自行排列;
grid() 為表格式排版, 元件是依據所指定的索引位置, 如同二維陣列元素一般放入表格中
place() 則可指定絕對或相對座標將元件精確擺放到視窗版面中.
'''
window.mainloop()
#步驟七、主視窗迴圈顯示
