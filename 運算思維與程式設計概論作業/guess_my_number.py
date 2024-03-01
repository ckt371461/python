import time
import random
def now():
    return time.time()
def one_to_hundred():
    return random.randint(1,100)
def guess_number(answer,guess,range):
    try:
        if (range[0]>guess) or (guess>range[1]):
            raise ValueError
        if guess == answer:
            range[0],range[1] = guess,guess 
            print('correct, the answer is %d'%answer)
        elif guess > answer:
            range[1] = guess
            print("it's too big, please enter a number between %d and %d: "%(range[0],range[1]))
        else :
            range[0] = guess
            print("it's too small, please enter a number between %d and %d: "%(range[0],range[1]))
    except ValueError:
        print("your number is not between %d and %d, please entering again "%(range[0],range[1]))
    return range
def game():
    start_time = now()
    range = [0,100]
    answer = one_to_hundred()
    guess_time = 0
    while range[0] != range[1]:
        guess = int(input("please enter a number between %d and %d: "%(range[0],range[1])))
        range = guess_number(answer,guess,range)
        guess_time+=1
    end_time = now()
    print('the total number of guesses is %d'%guess_time)
    print('total time to guess a number is %d seconds'%(end_time-start_time))
    print('your score is %d'%(10000/(guess_time*(end_time-start_time))))
game()
