import requests
import time
import sqlite3
import os
web='http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json'
def get_web(web,date,id):
    website = web+'&date='+date+'&stockNo='+id
    print(website)
    resp = requests.get(website)
    if resp.status_code != 200:
        print('the website is invalid')
        return None
    else:
        return resp.json() #json後面一定要加()，不然會發生TypeError: 'method' object is not subscriptable錯誤
def web_processing(web,date,id):
    form = list()
    resp = get_web(web,date,id)
    if resp:
        if resp["data"] :
            for data in resp["data"]:
                #各日成交資訊","fields":["日期","成交股數","成交金額","開盤價","最高價","最低價","收盤價","漲跌價差","成交筆數"]
                temporary = {
                    '日期' : data[0],
                    '開盤價' : data[3],
                    '收盤價' : data[6],
                    '成交筆數' : data[8]
                }
                form.append(temporary)
        return form
    else:
        return None
                
def execute_cmd(web,cmd):
    cursor = web.cursor()
    cursor.execute(cmd)
    web.commit()

DB_FILE = 'stockPrice.db' 
def main():
    #time.strftime() 函數可以依照指定的格式將 struct_time 時間資料轉換為文字輸出：
    #ex: %m/%d/%Y 輸出為 09/25/2019
    timenow = time.strftime('%Y%m%d')
    data = web_processing(web,timenow,'2330')
    '''
    sqlite3 為聯繫 SQLite 的資料庫 (database) 模組 (module) ，基本使用順序為
    用 connect() 函數建立跟資料庫檔案聯繫的 Connection 物件。
    由 Connection 物件的 cursor() 方法建立 Cursor 物件。
    利用 Cursor 物件的 execute() 方法進行資料庫操作。
    利用 Connection 物件的 commit() 方法做資料庫檔案更新。
    利用 Connection 物件的 close() 方法做關閉跟資料庫檔案的聯繫。
    '''
    if os.path.isfile(DB_FILE):
        os.remove(DB_FILE)

    db = sqlite3.connect(DB_FILE)
    execute_cmd(db,f'CREATE TABLE stockPrice (日期 TEXT, 開盤價 INTEGER, 收盤價 INTEGER, 成交筆數 INTEGER)')
    for datum in data:
        cmd = f'INSERT INTO stockPrice (日期,開盤價,收盤價,成交筆數) VALUES("{datum["日期"]}",{datum["開盤價"]},{datum["收盤價"]},{datum["成交筆數"].replace(",", "")})'
        #日期外面要在加""因為他是text",其他是integer 不用加，此外，因為成交筆數是最後一個，後方沒有,，因此要把最後的' '換成','
        # 因為 f' ... 是單引號開頭，再次碰到單引號就會被認為是結束，所以後方都得用雙引號

    
        execute_cmd(db,cmd)
    
    db.close()
if __name__ == '__main__':
    main()
