class Guess_game:
    def __init__(self,number,min=0,max=100):
        self.number=number
        self.min=min
        self.max=max
        self.guesses=0
    def guess(self):
        self.guesses+=1
        guessed_number=input(f"guess..({self.min}-{self.max})")
        if self.valid_number(guessed_number):
            return int(guessed_number)
        else:
            print('your guess is invalid..guess again')
            self.guess()

    def valid_number(self,number_in_range):
        try:
            number_in_range=int(number_in_range)
        except:
            print("you guesses an invalid number")
            return False
        return self.min<=number_in_range<=self.max
    def play(self):
        print('welcome..')
        while True:
            valid_guess=self.guess()
            if valid_guess<self.number:print('your guess was lower')
            elif valid_guess>self.number:print('your guess was higher')
            else:
                print('you have guessed in {} guesses great!'.format(self.guesses))
                self.play() if 's'==input('enter s') else exit()


g1=Guess_game(50)
g1.play()
