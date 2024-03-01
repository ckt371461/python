import pprint as pp
import requests,time
url = 'https://www.nkust.edu.tw/p/403-1000-1363-{}.php'
pages =list()
for page in range(1,4):
    pages.append(url.format(page)) 
for n,page in enumerate(pages,start=1):#數字放前面，不能放反    
    print(page)
    html = requests.get(page).text
    filename = 'page-{}.txt'.format(n)
    with open(filename,'wt',encoding= 'UTF-8') as fp:#沒加上encoding= 'UTF-8'會出現下面錯誤
        fp.write(html)
    time.sleep(3)
    print('{}done'.format(n))
'''
UnicodeEncodeError: 'cp950' codec can't encode character '\u5efb' in position 17392: illegal multibyte sequence

這主要原因為某個字元不是 code page 950 (cp950) 內有的字，而無法編碼寫進檔案裡面。
Python 處理字串預設是 Unicode 編碼，而在存檔案時，Python 會檢查命令提示字元的編碼頁 (此為 cp950) 做為檔案輸出的預設編碼頁，
因此會需要將 Unicode 字串皆轉為 cp950，若此時有字不在 cp950 內的話，就會出現此錯誤訊息。'''