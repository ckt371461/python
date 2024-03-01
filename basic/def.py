def get_initial(name,force_uppercase=True):
    if force_uppercase:
        initial = name[0:1].upper()
    else:
        initial = name[0:1]
    return initial
 
First_name = input('Please enter your first name: ')
First_name_initial = get_initial(First_name,False)

print('\n', First_name_initial) 
