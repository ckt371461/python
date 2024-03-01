from urllib import request
import json,csv
import time
url ='https://data.coa.gov.tw/Service/OpenData/FromM/FarmTransData.aspx'

with request.urlopen(url) as res:
    data = json.loads(res.read().decode())
with open('products.csv','w',encoding ='UTF-8',newline='') as fp:
    writer = csv.writer(fp)
    writer.writerow(('作物名稱','平均價','交易量'))#要額外再用括號刮起來，不然會有TypeError: writer.writerow() takes exactly one argument (3 given)錯誤
    for item in data:
        writer.writerow((item['作物名稱'],item['平均價'],item['交易量']))