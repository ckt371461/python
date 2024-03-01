def get_odd():
    return [i for i in range(10) if i%2==1]
count=1
for i in get_odd():
    if count == 3:
        print(f'The third number is: {i}')
        break
    count+=1