guess_me = 5
for number in range(10):
    if number<guess_me:
        print('Too Low')
    elif number>guess_me:
        print('Oops')
        break
    else:
        print('Find it')
        break
    