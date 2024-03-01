from datetime import date,timedelta
my_birthday=date(2004,5,7)
my_birthday_weekday=my_birthday.weekday()
my_birthday_isoweekday=my_birthday.isoweekday()
print(f'my birthday weekday = {my_birthday_weekday} , my birthday isoweekday = {my_birthday_isoweekday}')
# weekday()是0-6(0是星期一) isoweekday()是1-7(7是星期天)
ten_thousand_days=timedelta(days=10000)
my_birthday_add_ten_thousand_days=my_birthday+ten_thousand_days
print(my_birthday_add_ten_thousand_days)