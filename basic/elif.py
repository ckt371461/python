country = input('Enter your country: ') 

if country.lower() == 'canada': 

    province = input('Enter your province: ') 
    
    if province.lower() in('alberta',\
             'nunavaut','yukon' ):
    #if province.lower() == 'alberta' or province.lower() == 'nunavant':也可           
        tax = 0.05
    elif province.lower() == 'ontario':
        tax = 0.13     
    else:
        tax = 0.15   
else: 
    tax = 0          
print('Tax = ' + str(tax))