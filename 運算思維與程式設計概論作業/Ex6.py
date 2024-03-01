def triangle(number_to_start,half_of_height,length_of_paper):
    for i in range(number_to_start,half_of_height+number_to_start,2):
        for j in range(int((length_of_paper-i)/2)):
            print(' ',end = '')
        for j in range(i):
            print('$',end = '')
        for j in range(int((length_of_paper-i)/2)):
            print(' ',end = '')
        print('\n')
def rectangle(height,length_of_rectangle,length_of_paper):
    for i in range(height):
        for j in range(int((length_of_paper-length_of_rectangle)/2)):
            print(' ',end = '')
        for j in range(length_of_rectangle):
            print('I',end = '')
        for j in range(int((length_of_paper-length_of_rectangle)/2)):
            print(' ',end = '')
        print('\n')
for i in range(1,10,2):       
    triangle(i,5,50)
rectangle(5,3,50)