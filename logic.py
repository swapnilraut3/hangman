from words import bag_of_words
import random
from print_works import Print_works


class Play():
    '''
    This class implements core Hangman logic

    Attributes:
        total_lives (int) :     the count of total lives a player holds
        lost_lives (int):       the count of lives lost by player
        correct_guess (int):    the count of correct guess made by player
        won (boolean):          boolean flag to mark victory of player
        secret_word (str):      a secret word to be guessed by player,this is get-only attribute, can't be set by user
    '''

    def __init__(self, total_lives=7, lost_lives=0, correct_guess=0, won=False):
        '''constructor for Play class

        Attributes:
            total_lives (int) :     the count of total lives a player holds
            lost_lives (int):       the count of lives lost by player
            correct_guess (int):    the count of correct guess made by player
            won (boolean):          boolean flag to mark victory of player
            secret_word (str):      a secret word to be guessed by player
        '''
        super().__init__()
        self._total_lives = total_lives
        self._lost_lives = 0
        self._correct_guess = 0
        self._won = False
        self._secret_word = random.choice(bag_of_words)

    @property
    def secret_word(self):
        '''a secret word to be guessed by player 
        '''
        return self._secret_word

    @property
    def correct_guess(self):
        '''the count of correct guess made by player
        '''
        return self._correct_guess

    def correct_guess(self, value):
        '''set count of correct guess made by player
        '''
        self._correct_guess = value

    @property
    def won(self):
        '''returns boolean flag to mark victory of player
        true: win
        false: loose'''
        return self._won

    @won.setter
    def won(self, value):
        '''set flag to mark victory of player
        true: win
        false: loose
        '''
        self._won = value

    @property
    def lost_lives(self):
        '''the count of lives lost by player
        '''
        return self._lost_lives

    @lost_lives.setter
    def lost_lives(self, value):
        '''set the count of lives lost by player
        '''
        if value < self.lost_lives:
            raise ValueError(
                "New value of lost lives can't be less than older one")
        elif value > self.total_lives:
            raise ValueError(
                f"You can't set lost lives more than {self.total_lives}")
        else:
            self._lost_lives = value

    @property
    def total_lives(self):
        '''the count of total lives a player holds
        '''
        return self._total_lives

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
