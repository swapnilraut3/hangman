from print_works import Print_works
from global_store import Global_store

if __name__ == "__main__":
    myobj = Global_store()
    print_job = Print_works()

    lostLives = 0
    correct_guess = 0
    mylist = []
    unpresent_letters = []

    print_job.mask_secret_word(myobj.secret_word)

    mylist = list(myobj.secret_word)
    print_job.render_hangman()

    while lostLives != myobj.total_lives:
        print(print_job.masked_word)
        guess = input('Guess the letter: ')

        if guess in mylist:
            index = mylist.index(guess)
            mylist[index] = 'GUESSED'
            correct_guess += 1
            print_job.unmask_secret_letter(index, guess)
            print('Correct guess !!')
            if len(mylist) == correct_guess:
                myobj.won = True
                break
        else:
            lostLives += 1
            print(
                f'Wrong guess !! Lives remaining: {myobj.total_lives-lostLives} out of {myobj.total_lives}')
            if lostLives == 1:
                print_job.render_hangman(h='■')
            elif lostLives == 2:
                print_job.render_hangman(h='■', n='■')
            elif lostLives == 3:
                print_job.render_hangman(h='■', n='■', t='■')
            elif lostLives == 4:
                print_job.render_hangman(h='■', n='■', t='■', lh='■')
            elif lostLives == 5:
                print_job.render_hangman(h='■', n='■', t='■', lh='■', rh='■')
            elif lostLives == 6:
                print_job.render_hangman(
                    h='■', n='■', t='■', lh='■', rh='■', ll='■')
            elif lostLives == 7:
                print_job.render_hangman(
                    h='■', n='■', t='■', lh='■', rh='■', ll='■', rl='■')

            unpresent_letters.append(guess)
            print(f'Wrong guessed letter: {unpresent_letters}')

    else:
        myobj.won = False

    if myobj.won:
        print('You won!!')
    else:
        print('You lost')
        print(f'The correct word was: {myobj.secret_word}')
