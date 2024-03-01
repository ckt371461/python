guess_me = 7
number = 1
while True:
    if number<guess_me:
        print('Too Low')
    elif number>guess_me:
        print('Oops')
        break
    else:
        print('Find it')
        break
    number+=1
    