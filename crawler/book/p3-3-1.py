import requests
import csv,os
import time
url ='https://stats.moe.gov.tw/files/detail/110/110_student.csv'

csvdata = requests.get(url).text
rows = csvdata.split('\n')
tittle = rows[0].split(',')
data =list()
for row in rows[1:]:
    try:
        row = row.split(',')
        #Python replace() 方法把字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次。
        #ex:str.replace(old, new[, max])
        item = list()
        for i in range(1,5):
            item.append(row[i].replace('"',''))
        data.append(item)
    except:
        pass

filename = os.path.basename(url)
with open(filename,'w',encoding= 'UTF-8',newline='') as fp:
    writer = csv.writer(fp)
    writer.writerow(tittle[1:5])
    writer.writerows(data)
#返回path最后的文件名。若path以/或\结尾，那么就会返回空值。
