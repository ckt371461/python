def guess_word(character,term,right_term):
    for i in range(len(term)):
        if term[i] == character:
            right_term[i] = term[i]     
    return right_term
with open('guess word.txt','r') as file:
    lines = file.readlines()
term_list = []
for line in lines:
    term_list.append(line.strip())

def guess_game(list):
    correct = 0 
    wrong = 0
    for term in list:
        right_term = ['*']*len(term)
        while ''.join(right_term) != term:
            character = input('Enter a letter to guess a length %d word :'%(len(term)))
            if character == 'stop':
                break
            right_term_old = right_term.copy()
            right_term = guess_word(character,term,right_term)
            if right_term_old == right_term:
                wrong += 1
            else:
                correct += 1
            print(right_term)
        print('Congratulations! The answer is %s!'%term)
    print('Number of correct guesses: %d times\nNumber of wrong guesses: %d times'%(correct,wrong))
    print('Your score: %d'%((correct*20)+(wrong*-20)/(correct + wrong)))
guess_game(term_list)




