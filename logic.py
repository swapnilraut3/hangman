from words import bag_of_words
import random
from print_works import Print_works

total_lives = (7,)
lostLives = 0
correct_guess = 0
mylist = []
unpresent_letters = []
won = True

secret_word = random.choice(bag_of_words)

print_job = Print_works()
print_job.mask_secret_word(secret_word)

mylist = list(secret_word)
print_job.render_hangman()

while lostLives != total_lives[0]:
    print(print_job.masked_word)
    guess = input('Guess the letter: ')

    if guess in mylist:
        index = mylist.index(guess)
        mylist[index] = 'GUESSED'
        correct_guess += 1
        print_job.unmask_secret_letter(index, guess)
        print('Correct guess !!')
        if len(mylist) == correct_guess:
            won = True
            break
    else:
        lostLives += 1
        print(
            f'Wrong guess !! Lives remaining: {total_lives[0]-lostLives} out of {total_lives[0]}')
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
    won = False

if won:
    print('You won!!')
else:
    print('You lost')
    print(f'The correct word was: {secret_word}')
