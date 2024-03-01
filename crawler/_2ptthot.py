import requests
from bs4 import BeautifulSoup
import json
import time
ptt_url = 'http://www.ptt.cc'
cookies={'over18': '1'}
def get_web_page(url):
    resp = requests.get(url, cookies=cookies)
    if resp.status_code == 200:#注意不要寫成 if resp == 200
        return resp.text
    else:
        print('url is invalid.')
        return None
def get_articles(dom,data):
    '''
    文件物件模型（Document Object Model, DOM)是HTML、XML 和SVG 文件的程式介面。 
    它提供了一個文件（樹）的結構化表示法，並定義讓程式可以存取並改變文件架構、風格和內容的方法。
    DOM 提供了文件以擁有屬性與函式的節點與物件組成的結構化表示。
    '''
    soup = BeautifulSoup(dom,'html5lib')
    paging_div = soup.find('div','btn-group btn-group-paging')
    #div是division這個單字取前面三個字母來表示，division是區分的意思，div標籤主要的功能就是在形成一個個的區塊，方便網頁排版美化。

    #PTT下一頁的網址出現在 class 為 btn-group btn-group-paging 的 div 下的第二個子元素 a 的 href 屬性中
    prev_url = paging_div.find_all('a')[1]['href']
    #找出所有 <a href=....> 之後，取第 1 個 <a href=....> 然後再取其中的 href 的文字

    #我們看到href前面通常都會有個＜a＞標籤，這個 a 代表連結的意思，當然也會有人稱 a 為link，但都是相同的功能與意義。
    articles = []
    divs = soup.find_all('div', 'r-ent')
    #我們需要的資訊都放在 CSS 類別為 r-ent 的 <div></div> 中，包含推文數，作者 id，文章標題與發文日期。
 
    for d in divs:
        # If post date matched:
        if d.find('div', 'date').text.strip() == data:
            '''
            Python strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。 
            注意：该方法只能删除开头或是结尾的字符，不能删除中间部分的字符。
            '''
            # To retrieve the push count:
            push_count = 0
            push_str = d.find('div', 'nrec').text
            if push_str:
                try:
                    push_count = int(push_str)
                except ValueError:
                    # If transform failed, it might be '爆', 'X1', 'X2', etc.
                    if push_str == '爆':
                        push_count = 99
                    elif push_str.startswith('X'):
                        push_count = -10

            # To retrieve title and href of the article:
            if d.find('a'):
                href = d.find('a')['href']
                title = d.find('a').text
                author = d.find('div', 'author').text if d.find('div', 'author') else ''
                articles.append({
                    'title': title,
                    'href': href,
                    'push_count': push_count,
                    'author': author
                })

    return articles, prev_url

def get_author_ids(posts, pattern):
    ids = set()
    for post in posts:
        if pattern in post['author']:
            ids.add(post['author'])
    return ids

def main():
    current_page = get_web_page(ptt_url + '/bbs/Gossiping/index.html')
    if current_page:
        # To keep all of today's articles.
        articles = []
        # Today's date, here we remove the 0 at the head to match the format of PTT date.
        # API doc for strftime: https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
        # API doc for lstrip: https://www.tutorialspoint.com/python/string_lstrip.htm
        today = time.strftime("%m/%d").lstrip('0')
        current_articles, prev_url = get_articles(current_page, today)

        while current_articles:
            articles += current_articles
            current_page = get_web_page(ptt_url  + prev_url)
            current_articles, prev_url = get_articles(current_page, today)

        print("Today's 5566:")
        print(get_author_ids(articles, '5566'))

        print('\nThere are ', len(articles), ' posts today.')
        threshold = 50
        print('Hot post(≥ %d push): ' % threshold)
        for article in articles:
            if int(article['push_count']) > threshold:
                print(article)
        # with as: https://openhome.cc/Gossip/Python/WithAs.html
        # json.dump: http://python3-cookbook.readthedocs.io/zh_CN/latest/c06/p02_read-write_json_data.html
        with open('gossiping.json', 'w', encoding='UTF-8') as file:
            json.dump(articles, file, indent=2, sort_keys=True, ensure_ascii=False)


if __name__ == '__main__':
    main()

