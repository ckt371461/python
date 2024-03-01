from datetime import date,datetime
today=date.today()
with open('today.txt','wt') as td:
    td.write(today.isoformat())
    #用 isoformat() 輸出日期
    print(f'Today is {today}')
