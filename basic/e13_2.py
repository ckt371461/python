with open('today.txt','rt') as td:
    today_string=td.read()
import time
fmt=r'%Y-%m-%d'
today=time.strptime(today_string,fmt)
#tm_year（年）、tm_mon（月）、tm_mday（日）、tm_hour（时）、tm_min（分）、tm_sec（秒）、
#tm_wday（weekday0 - 6（0表示周1））、tm_yday（一年中的第几天1 - 366）、tm_isdst（是否是夏令时）
print(today)