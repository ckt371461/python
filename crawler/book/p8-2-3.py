import requests,time
from pymongo import MongoClient
from bs4 import BeautifulSoup
url = 'https://www.nkust.edu.tw/p/403-1000-1363-{}.php'
data =list()

for page in range(1,6):
    html = requests.get(url.format(page)).text
    soup=BeautifulSoup(html,'html5lib')
    sel='#pageptlist > div > div > div > div.d-txt > div.mtitle'
    target=soup.select(sel)
    for item in target:
        pdate=item.i.text.strip()
        title=item.a.text.strip()
        link=item.a['href']
        #pageptlist > div > div > div > div.d-txt > div.mtitle > i
        data.append((pdate,link,title))
    time.sleep(3)

conn=MongoClient()
db=conn.news
collection=db.nkust


for article in data[:5]:#內容太大只取出前五項內容
    content=dict()
    url=article[1]
    content['date']=article[0]
    content['title']=article[2]
    print(url)
    html = requests.get(url).text
    soup=BeautifulSoup(html,'html5lib')
    sel='#Dyn_2_3 > div.module.module-detail.md_style1 > div > section > div.mcont > div.mpgdetail p'
    target=soup.select(sel)
    content['content']=""
    for item in target:
        try:
            content['content']+=item.text
        except:
            content['content']+=''
            pass
    try:
        collection.insert_one(content)
    except:
        pass
    time.sleep(3)
print('Done')
   