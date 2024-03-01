import requests
import time
url_api = 'http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json'
import json
import csv
fields = ["日期","成交股數","成交金額","開盤價","最高價","最低價","收盤價","漲跌價差","成交筆數"]
def get_web_data(date,id,url=url_api):
    resp = requests.get(url+'&date='+date+'&stockNo='+id)
    if resp.status_code != 200:
        print('url is invalid')
        return None
    else:
        return resp.json()
def data_processing(date,id):
    resp = get_web_data(date,id)
    #各日成交資訊","fields":["日期","成交股數","成交金額","開盤價","最高價","最低價","收盤價","漲跌價差","成交筆數"]
   
    form = list()
    
    if resp:
        if resp["data"] :
            for data in resp["data"]:
                record = list()
                for field in range(len(fields)):
                    record.append(data[field])
                form.append(record)
                del record     
            return form
    else:
        return None
def main():
    outp = list()
    stock_id = '2330'
    current_date = time.strftime('%Y%m%d')
    current_year = time.strftime('%Y')
    current_month = time.strftime('%m')
    print('取得本月台積電 (2330) 的股價 %s %s...' % (current_year, current_month))
    collected_info = data_processing(current_date,stock_id)
    for info in collected_info:
        remember = list()
        for a in range(len(info)):
            remember.append(fields[a]+'='+info[a])
            outp.append(remember)
        print(remember)
    with open('stockPrice.json', 'w', encoding='UTF-8') as file:#寫成.json檔(要先import json)
            json.dump(outp, file, indent=2, sort_keys=True, ensure_ascii=False)
            #如果 ensure_ascii 是 true （即默认值），输出保证将所有输入的非 ASCII 字符转义。如果 ensure_ascii 是 false，这些字符会原样输出。
            # ex: '日' '期' 會等於 '\u65e5' '\u671f'
            #如果 sort_keys 是 true（默认为 False），那么字典的输出会以键的顺序排序
            #https://docs.python.org/zh-tw/3/library/json.html
    
    with open('stockThisMonth.csv', 'w', encoding='UTF-8', newline='') as file:#寫成.csv檔(要先import csv)
        writer = csv.writer(file)
        writer.writerow(('日期', '開盤價', '收盤價', '成交筆數'))
        for info in collected_info:
            writer.writerow([info[0], info[3], info[6], info[8].replace(',', '')])
        


if __name__ == '__main__':
    main()
