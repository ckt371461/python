from selenium import webdriver
from bs4 import BeautifulSoup
import time
url='https://www.cwb.gov.tw/V8/C/W/OBS_County.html?ID={}'
web=webdriver.Chrome('chromedriver.exe')
web.implicitly_wait(60)
web.get(url.format('68'))
html = web.page_source
time.sleep(10)
web.quit()
soup = BeautifulSoup(html,'html5lib')
sel='#stations > tr'
rows = soup.select(sel)
data = list()
for row in rows:
    try:
        header = row.find_all('th')
        fields = row.find_all('td')
        observing_time = fields[0].text
        data.append((header[0].a.text.strip(),float(fields[1].text),int(fields[7].text)))#外面記得加()表示這是一個元組，不然會出錯
        #<th scope="row" headers="station" data-href="OBS_Station.html?ID=46705" title="進入新屋測站24小時資料" class="is_show">
        #   <a href="javascript:void(0)">
        #       新屋
        #   </a>
        #</th>
        #<td headers="temp" class="is_show" style="min-height: 46px;">23.0</td>  fields[1](溫度)
        #<td headers="hum" style="min-height: 46px;">78</td>                     fields[7](濕度)
    except:
        pass
print('最近觀察時間',observing_time)
print(data)
