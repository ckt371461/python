from datetime import datetime , timedelta
birthday = input('Please enter your birthday(dd/mm/yyyy): ')
birthday_date = datetime.strptime(birthday, '%d/%m/%Y')
print('      Birthday:      ' + str(birthday_date))
 
one_day = timedelta(days=1)
birthday_even = birthday_date - one_day
print('Day before Birthday: ' + str(birthday_even))