import requests
from bs4 import BeautifulSoup
import json
headers= {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9,zh-TW;q=0.8,zh;q=0.7,zh-CN;q=0.6,ja;q=0.5',
    'referer' :'https://www.google.com/',
    'content-length': '828',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://www.dcard.tw',
    'referer': 'https://www.dcard.tw/',
    'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
  }

cookies ={
    'CFFPCKUUID':'2363-bmmIYBpnUugTaP4S96tWBnrGRMSdbDZu',
    'CFFPCKUUIDMAIN':'2504-erGjZyapKjiTp3A1H0Xuk5ytbqk8sfLs',
    '_cfuvid':'a3tQP6UKTbcOVJ.HwEVKb7rCWahJtb7hO5oQt2HGhrg-1667129116030-0-604800000',
    'dcard-web-oauth-tk':'eyJhY2Nlc3NUb2tlbiI6ImV5SmhiR2NpT2lKRlpFUlRRU0lzSW10cFpDSTZJbEpMTFVoZlRUUm9VVkpET1dzeFUxcEdZMEZ1UkRBMVZreFljV1JZUm1kUVZYQXdWbGx0YjJ4eWFqZzlJbjAuZXlKaGNIQWlPaUpqTW1VM05qTTVOUzB6T0dFeExUUTRaamN0WVRsbE1DMWhaamN6TldJNFpqZGpOREVpTENKbGVIQWlPakUyTmpjeE1qazBNVFlzSW1saGRDSTZNVFkyTnpFeU9URXhOaXdpYVhKMElqb2lOek0yTURReVpUUXROV1F6TlMwME1qUmhMV0V5WTJZdE5EY3hNbVk1T1RZd1pETXpJaXdpYVhOeklqb2laR05oY21RaUxDSnFkR2tpT2lKa05XUXhOVGxtWlMwNU5qazNMVFExWkdNdFlqRXlaUzB6TlRCaFlUTTRPVE13TURnaUxDSnpZMjl3WlhNaU9sc2liV1Z0WW1WeUlpd2liV1Z0WW1WeU9uZHlhWFJsSWl3aVpXMWhhV3dpTENKbGJXRnBiRHAzY21sMFpTSXNJbVJsZG1salpTSXNJbVJsZG1salpUcDNjbWwwWlNJc0luQm9iM1J2SWl3aWJtOTBhV1pwWTJGMGFXOXVJaXdpWm05eWRXMGlMQ0ptYjNKMWJUcHpkV0p6WTNKcFltVWlMQ0p3YjNOMElpd2ljRzl6ZERwemRXSnpZM0pwWW1VaUxDSm1ZV05sWW05dmF5SXNJbkJvYjI1bElpd2ljR2h2Ym1VNmRtRnNhV1JoZEdVaUxDSndhRzl1WlRwM2NtbDBaU0lzSW5CbGNuTnZibUVpTENKd1pYSnpiMjVoT25OMVluTmpjbWxpWlNJc0ltTnZibVpwWnlJc0ltTnZibVpwWnpwM2NtbDBaU0lzSW5SdmEyVnVPbkpsZG05clpTSXNJbWxrWTJGeVpDSXNJblJ2Y0dsaklpd2lkRzl3YVdNNmMzVmljMk55YVdKbElpd2labVZsWkRwemRXSnpZM0pwWW1VaUxDSnNiMmRwYmxabGNtbG1hV05oZEdsdmJpSXNJbXh2WjJsdVZtVnlhV1pwWTJGMGFXOXVPblpsY21sbWVTSXNJbU52Ykd4bFkzUnBiMjRpTENKamIyeHNaV04wYVc5dU9uZHlhWFJsSWl3aVpuSnBaVzVrSWl3aVpuSnBaVzVrT25keWFYUmxJaXdpYldWemMyRm5aU0lzSW0xbGMzTmhaMlU2ZDNKcGRHVWlMQ0p3YjJ4c09uZHlhWFJsSWl3aWFXUmxiblJwZEhrNmRtRnNhV1JoZEdWa0lpd2liR2xyWlNJc0luSmxZV04wYVc5dUlpd2ljRzl6ZERwM2NtbDBaU0lzSW1OdmJXMWxiblE2ZDNKcGRHVWlMQ0p5WlhCdmNuUWlMQ0prYjNkdWRtOTBaU0pkTENKemRXSWlPaUl4TVRrME56azBOeUo5LnNqazJsTnJ1V2cxaW5teDU4WlJqVUpfMFN2SE4zR0Eza3R5bVFGdlBPdmV6RXhQS1JTRVhCN3pkbFV1VkYzQ0NpSzVESVFlblNwckVPaXJWbUxUVkF3IiwidG9rZW5UeXBlIjoiQmVhcmVyIiwicmVmcmVzaFRva2VuIjoiejEveHAyMlRRVTZnbjg5N1lIcnExUT09IiwiZXhwaXJlc0F0IjoiMjAyMi0xMC0zMFQxMTozMDoxNi4wMDBaIn0=',
    'dcard-web-oauth-tk.sig':'6cF0C72L2ZuCiYcaKCsq3siPaSU', 
    'gcl_au':'1.1.1235472430.1667129118',
    '_gid':'GA1.2.419088184.1667129118',
    '_gat':'1',
    '_ga':'GA1.1.450632032.1667129118',
    '_ga_C3J49QFLW7':'GS1.1.1667129118.1.1.1667129118.0.0.0',
    '_fbp':'fb.1.1667129118123.1248492404',
    '__gads=ID':'5e20f7c26bbda035:T=1667129118:S=ALNI_Mag45WNl164jKCrgqO-4dAUZTsldQ',
    '__gpi=UID':'00000b7183728d56:T=1667129118:RT=1667129118:S=ALNI_MbAIMRlRCF-wRoo_D6VSovYbRYCqw'
    }
dcard_url = 'https://www.dcard.tw/f'
def get_web_page(url):
    requests.session
    resp = requests.get(url,headers=headers,cookies=cookies)
    if resp.status_code == 200:#注意不要寫成 if resp == 200
        return resp.text
    else:
        print('url is invalid.')
        return None
def get_articles(dom):
    #<h2 class="sc-299efbf1-2 hzbfrA">
    #   <a class="sc-299efbf1-3 qnlFC" href="/f/rainbow/p/240380091">
    #       <span>麻煩不要只負責脫好嗎？！</span>
    #   </a>
    # </h2>
    '''
    文件物件模型（Document Object Model, DOM)是HTML、XML 和SVG 文件的程式介面。 
    它提供了一個文件（樹）的結構化表示法，並定義讓程式可以存取並改變文件架構、風格和內容的方法。
    DOM 提供了文件以擁有屬性與函式的節點與物件組成的結構化表示。
    '''
    soup = BeautifulSoup(dom,'html5lib')
    articles = []
    divs = soup.find_all('a', 'sc-299efbf1-3 qnlFC')
 
    for d in divs:
        if d.find('span'):
            span = d.find('sapn')
            url = d.find('href')
            articles.append({
                'span': span,
                'url': url
            })

    return articles
def main():
    current_page = get_web_page(dcard_url )
    if current_page:
        articles = get_articles(current_page)
        with open('dcard.json', 'w', encoding='UTF-8') as file:
            json.dump(articles, file, indent=2, sort_keys=True, ensure_ascii=False)


if __name__ == '__main__':
    main()

