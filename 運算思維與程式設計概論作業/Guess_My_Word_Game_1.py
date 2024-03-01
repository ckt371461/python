def guess_word(guess,term,right_term):
    if len(term) == len(guess):
        for i in range(len(term)):
            if term[i] == guess[i]:
                right_term[i] = term[i]
    else:
        print('The number of character is wrong')        
    return right_term
with open('guess word.txt','r') as file:
    lines = file.readlines()
term_list = []
for line in lines:
    term_list.append(line.strip())

def guess_game(term_list):
    correct = 0 
    wrong = 0
    for term in term_list:
        right_term = ['*']*len(term)
        while True:
            guess = input('Enter a length %d word start with %s:'%(len(term),term[0]))
            if guess == 'stop':
                break
            if guess == term:
                print('Congratulations! The answer is %s!'%term)
                correct +=1
                break
            right_term = guess_word(guess,term,right_term)
            wrong +=1
            print(right_term)
    print('Number of correct guesses: %d times\nNumber of wrong guesses: %d times'%(correct,wrong))
    print('Your score: %d'%((correct*100)+(wrong*-20)))
guess_game(term_list)



