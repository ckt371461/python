import tkinter as tk
import tkinter.messagebox as mb
def guess_word(guess,term,right_term):
    if len(term) == len(guess):
        for i in range(len(term)):
            if term[i] == guess[i]:
                right_term[i] = term[i]
    else:
        print('The number of character is wrong')        
    return right_term
term_list = ['test','python','email']

def guess_game(term_list):
    window=tk.Tk()
    window.wm_title('Guess My Word Game')
    correct = 0 
    wrong = 0
    for term in term_list:
        right_term = ['*']*len(term)
        guess = ['*']*len(term)
        while True:
            guess_tk=tk.StringVar()
            label1=tk.Label(window,text='Enter a length %d word start with %s:'%(len(term),term[0]))
            label1.pack()
            entry1=tk.Entry(window)
            entry1.pack()
            def event1():
                while True:
                    guess_tk.set(entry1.get())
                    guess = guess_tk.get()
                    if len(guess) != len(term):
                        mb.showerror("Error", "The length of your guess is incorrect. Try again.")
                        return
                    else:
                        break
            button1=tk.Button(window,text='送出',command=event1)
            button1.pack()
            if guess == 'stop':
                break
            if guess == term:
                label2=tk.Label(window,text='Congratulations! The answer is %s!'%term)
                label2.pack()
                correct +=1
                break
            right_term = guess_word(guess,term,right_term)
            wrong +=1
            label3=tk.Label(window,text=right_term)
            label3.pack()
            window.mainloop()

        
    print('Number of correct guesses: %d times\nNumber of wrong guesses: %d times'%(correct,wrong))
    print('Your score: %d'%((correct*100)+(wrong*-20)))
guess_game(term_list)