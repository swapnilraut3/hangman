class Global_store():
    '''
    This class stores Global constants

    Attributes:
        total_lives (int) :     the count of total lives a player holds
        lost_lives (int):       the count of lives lost by player
        correct_guess (int):    the count of correct guess made by player
        won (boolean):          boolean flag to mark victory of player
    '''

    def __init__(self, total_lives=7, lost_lives=0, correct_guess=0, won=False):
        '''constructor for Global_store class

        Attributes:
            total_lives (int) :     the count of total lives a player holds
            lost_lives (int):       the count of lives lost by player
            correct_guess (int):    the count of correct guess made by player
            won (boolean):          boolean flag to mark victory of player
        '''
        super().__init__()
        self._total_lives = total_lives
        self._lost_lives = 0
        self._correct_guess = 0
        self._won = False

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

    @total_lives.setter
    def total_lives(self, value):
        '''set the count of total lives a player holds
        '''
        if value < self._total_lives:
            self._total_lives = value
        else:
            raise ValueError("You can't increase lives")
