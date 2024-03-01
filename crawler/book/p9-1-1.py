import requests,json
from bs4 import BeautifulSoup
#PChome適用動態網頁技術，用開發人員工具查詢他results裡面的網址
url='https://ecshweb.pchome.com.tw/search/v3.3/all/results?q=mac%20mini&page=1&sort=sale/dc'
html=requests.get(url).text
products=json.loads(html)['prods']
for product in products:
    if product['price']>20000:
        print('NT$:{},{}'.format(product['price'],product['name']))