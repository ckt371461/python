def leap_year(year):
    if year % 1000 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else: return False
   
print('leap_year(1004)=', leap_year(1004))
print('leap_year(1000)=', leap_year(1000))
print('leap_year(1300)=', leap_year(1300))
print('leap_year(1555)=', leap_year(1555))