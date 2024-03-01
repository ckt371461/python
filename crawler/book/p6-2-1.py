from selenium import webdriver
import time
from bs4 import BeautifulSoup
url='https://www.cwb.gov.tw/V8/C/W/OBS_County.html?ID={}'
web = webdriver.Chrome('chromedriver.exe')
web.implicitly_wait(60)
web.get(url.format('menu'))
html = web.page_source
time.sleep(10)
web.quit()
soup = BeautifulSoup(html,'html5lib')
target = soup.select('#County option')
#<select id="County">
#   <optgroup label="北部" id="N">
#       <option value="10017">基隆市    
# 因為要指定的是最外面的ID，因此用 #id 這個選擇方法 ，空白是指匹配所有option子元素
counties = list()
for item in target:
    counties.append((item.text,item['value']))#外面那個括號表示用元組的方式儲存
print(counties)
for county in counties:
    print(county[0],"的網址是",url.format(county[1]))