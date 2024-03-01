import requests,time,sqlite3
from bs4 import BeautifulSoup
url = 'https://www.nkust.edu.tw/p/403-1000-1363-{}.php'
titles =list()
for page in range(1,11):
    html = requests.get(url.format(page)).text
    soup=BeautifulSoup(html,'html5lib')
    sel='#pageptlist > div > div > div > div.d-txt > div.mtitle > a'
    data=soup.select(sel)
    for item in data:
        titles.append((item['title'],item['href']))
    time.sleep(3)
db=sqlite3.connect('headlines.db')
cur=db.cursor()
sql="insert into titles (title,link) values(?,?)"
for title in titles:
    cur.execute(sql,title)
    print(title)
db.commit()
db.close()
print('Done')

    