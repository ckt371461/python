import requests
from bs4 import BeautifulSoup

def main():
    web ='http://blog.castman.net/web-crawler-tutorial/ch1/connect.html'
    try: 
        data = requests.get(web)
    except:
        data = None
    if data != 0 and data.status_code == 200:
        print('data.status_code = ',data.status_code)
        #print(data.text)
        soup = BeautifulSoup(data.text,'html.parser')
        
        try:
            h1 = soup.find('h1')
        except:
            h1 = None
       
        if h1:
            print(h1)
            print(h1.text)
        else:
            print('h1 tag not found!')
        
        try:
            h2 = soup.find('h2')
        except:
            h2 = None
       

        if h2:
            print(h2)
            print(h2.text)
        else:
            print('h2 tag not found!') 
if  __name__ == '__main__':
    main()
        