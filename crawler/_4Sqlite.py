import csv
import sqlite3
#Connection()的引數列表
# host，連線的資料庫伺服器主機名，預設為本地主機(localhost)。
# user，連線資料庫的使用者名稱，預設為當前使用者。
# passwd，連線密碼，沒有預設值。
# db，連線的資料庫名，沒有預設值。
# conv，將文字對映到Python型別的字典。
import os
# os.sep 更改作業系統中的路徑分隔符。
# os.getcwd()獲取當前路徑，這個在Python程式碼中比較常用。
# os.listdir() 列出當前目錄下的所有檔案和資料夾。
# os.remove() 方法可以刪除指定的檔案。
# ｏs.system() 方法用來執行shell命令。
# os.chdir() 改變當前目錄，到指定目錄中。



def execute_sql(db, sql_cmd):#對db這個檔案執行sql_cmd這個動作
    cursor = db.cursor()
    cursor.execute(sql_cmd)
    #執行sql_cmd的指令
    db.commit()
    #提交至sql_cmd，该commit()方法用于确认用户对数据库所做的更改。
    # 每当使用 update 或任何其他语句对数据库进行任何更改时，都必须提交更改。
    # 如果我们commit()在对数据库进行任何更改后不使用该方法，则不会更新数据库，也不会反映更改。

STOCK_DB_FILE = 'stockPrice.db'
if os.path.isfile(STOCK_DB_FILE):
    #OS 模塊 ，這個是調用操作系統命令，來達成建立文件，刪除文件，查詢文件等目的
    # os.path 模块主要用于获取文件的属性
    #os.path.isfile(path)	判断路径是否为文件
    # https://www.runoob.com/python/python-os-path.html
    os.remove(STOCK_DB_FILE)
    # os.remove() 方法可以刪除指定的檔案。

db = sqlite3.connect(STOCK_DB_FILE)
'''
sqlite3 為聯繫 SQLite 的資料庫 (database) 模組 (module) ，基本使用順序為

用 connect() 函數建立跟資料庫檔案聯繫的 Connection 物件。
由 Connection 物件的 cursor() 方法建立 Cursor 物件。
利用 Cursor 物件的 execute() 方法進行資料庫操作。
利用 Connection 物件的 commit() 方法做資料庫檔案更新。
利用 Connection 物件的 close() 方法做關閉跟資料庫檔案的聯繫。
'''
execute_sql(db, f'CREATE TABLE stockPrice (日期 TEXT, 開盤價 INTEGER, 收盤價 INTEGER, 成交筆數 INTEGER)')

with open('stockThisMonth.csv', newline='', encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    #csv.DictReader(csvfile) 可以用「字典」的型態，讀取 CSV 檔案，讀取後可以使用字典的操作方式，將每一行 ( row ) 印出
    print('日期', '開盤價','收盤價','成交筆數')
    for info in reader:
        print(info['日期'],info['開盤價'],info['收盤價'],info['成交筆數'])
        command = f'INSERT INTO stockPrice (日期, 開盤價, 收盤價, 成交筆數) VALUES("{info["日期"]}", {info["開盤價"]}, {info["收盤價"]}, {info["成交筆數"]})'
        print('command=', command)
        execute_sql(db, command)

db.close()
#連線物件的db.close()方法可關閉資料庫連線，並釋放相關資源。