import requests
from bs4 import BeautifulSoup
url='https://www.ptt.cc/bbs/gossiping/index.html'
session=requests.Session()
#<input type="hidden" name="from" value="/bbs/gossiping/index.html">
#<button class="btn-big" type="submit" name="yes" value="yes">我同意，我已年滿十八歲<br><small>進入</small></button>
payload={
    'from':'/bbs/gossiping/index.html',
    'yes':'yes'
}  
#送出表單
session.post('https://www.ptt.cc/ask/over18?from=%2Fbbs%2Fgossiping%2Findex.html',payload)
#   %2F表示ASCII码0x2F(47)对应的字符, 即/
# 所以網址為https://www.ptt.cc/ask/over18?from=/bbs/gossiping/index.html
html=session.get(url).text
soup=BeautifulSoup(html,'html5lib')
titles = soup.select('.title')
'''
因為title是一個class因此前面放.代表選取所有class為tittle的元素
<div class="title">			
    <a href="/bbs/Gossiping/M.1667720643.A.C4B.html">Re: [問卦] 這樣深蹲有標準嗎？</a>			
</div>
'''
for title in titles:
    print(title.a.text)
    print('https://www.ptt.cc'+title.a['href'])
    #因為href是a下的一個屬性，因此用[]選取屬性