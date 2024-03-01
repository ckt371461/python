import requests,json
from bs4 import BeautifulSoup
#PChome適用動態網頁技術，用開發人員工具查詢他results裡面的網址
def send_simple_message(title,body):
	return requests.post(
		"https://api.mailgun.net/v3/sandbox15e7fc737e2f48d4b9fda5ec87c1bdc8.mailgun.org/messages",
		auth=("api", "e48db7b2db4e5acdf5a4c8d7a6a76c52-48c092ba-ccde8a9f"),
		data={"from": "Excited User <cktim371461@gmail.com>",
			"to": ["cktim371461@gmail.com"],
			"subject": "{}".format(title),
			"text": "{}".format(body)})
url='https://ecshweb.pchome.com.tw/search/v3.3/all/results?q=mac%20mini&page=1&sort=sale/dc'
html=requests.get(url).text
products=json.loads(html)['prods']
message=''
for product in products:
    if product['price']>20000:
        message+='NT$:{},{}\n'.format(product['price'],product['name'])

send_simple_message('Mac Mini價格通知',message)
print('Done')