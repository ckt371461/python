from datetime import datetime, timedelta
current_datetime = datetime.now()
print('Today is: ' + str(current_datetime))

one_day = timedelta(days=1)
yesterday = current_datetime - one_day
print('Yesterday is: ' + str(yesterday))

one_week = timedelta(weeks=1)
last_week = current_datetime - one_week
print('Last_week is: ' + str(last_week))

print('   Day    is: ' +   str(current_datetime.day))
print('   Month  is: ' + str(current_datetime.month))
print('   Year   is: ' + str(current_datetime.year))
print('   Hour   is: ' + str(current_datetime.hour))
print('   Minute is: ' + str(current_datetime.minute))
print('   Second is: ' + str(current_datetime.second))
