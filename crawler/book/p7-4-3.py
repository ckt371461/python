import requests,mysql.connector
from bs4 import BeautifulSoup
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}
html=requests.get('https://www.books.com.tw/web/sys_saletopb/books/19/?loc=P_0002_020',headers=headers).text
soup=BeautifulSoup(html,'html5lib')
sel='li.item'
ranking=soup.select(sel)
conn = mysql.connector.connect(
    host='localhost',
    database='books',
    user='root',
    password='#Cktim082371461'
)
cursor=conn.cursor()
#MySQL強烈要求加上``，這個在數字一的左邊
#注意資料型態，在字元加上''，而rank因為是整數所以不用加''
sql='''
insert into `ranking30` (`rank`,`title`,`author`,`price`) values ({},'{}','{}','{}');
'''
for rank,book in enumerate(ranking,start=1):
    try:
        title=book.h4.a.text
        detail = book.find_all('li')
        author=detail[0].text
        price=detail[1].text#有些沒有作者，因此不加上TRY的話有可能出錯
        try:
            cursor.execute(sql.format(rank,title,author,price))
        except mysql.connector.Error as error:
            print('Error:{}'.format(error))
            pass
        conn.commit()
    except:
        pass
        
conn.close()
print('Done')