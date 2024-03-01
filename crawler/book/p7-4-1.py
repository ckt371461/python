import requests
from bs4 import BeautifulSoup
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}
html=requests.get('https://www.books.com.tw/web/sys_saletopb/books/19/?loc=P_0002_020',headers=headers).text
soup=BeautifulSoup(html,'html5lib')
sel='li.item'
ranking=soup.select(sel)
for no,book in enumerate(ranking,start=1):
    try:
        print('第{}名'.format(no))
        print(book.h4.a.text)
        detail = book.find_all('li')
        print(detail[0].text)
        print(detail[1].text)#有些沒有作者，因此不加上TRY的話有可能出錯
        print("-------------------------")
    except:
        pass