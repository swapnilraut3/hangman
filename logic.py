from print_works import Print_works
from global_store import Global_store

if __name__ == "__main__":
    store = Global_store()
    print_job = Print_works()

    lostLives = 0
    mylist = []
    unpresent_letters = []

    print_job.mask_secret_word(store.secret_word)

    mylist = list(store.secret_word)
    print_job.render_hangman()

    while lostLives != store.total_lives:
        print(print_job.masked_word)
        guess = input('Guess the letter: ')

        if guess in mylist:
            index = mylist.index(guess)
            mylist[index] = 'GUESSED'
            store.correct_guess += 1
            print_job.unmask_secret_letter(index, guess)
            print('Correct guess !!')
            if len(mylist) == store.correct_guess:
                store.won = True
                break
        else:
            lostLives += 1
            print(
                f'Wrong guess !! Lives remaining: {store.total_lives-lostLives} out of {store.total_lives}')
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
        store.won = False

    if store.won:
        print('You won!!')
    else:
        print('You lost')
        print(f'The correct word was: {store.secret_word}')
