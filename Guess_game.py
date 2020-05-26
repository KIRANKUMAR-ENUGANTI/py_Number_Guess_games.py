class Guess_game:
    def __init__(self,number,min=0,max=100):    #actual number ,to check the guessed number is in rage of min and max
        self.number=number
        self.min=min
        self.max=max
        self.guesses=0  #let the guess be 0 first
    def guess(self):
        self.guesses+=1     #for evert valid and invalid guess 
        guessed_number=input(f"guess..({self.min}-{self.max})")
        if self.valid_number(guessed_number):   #if guessednumber in range or not
            return int(guessed_number)
        else:
            print('your guess is invalid..guess again')
            self.guess()    #if not in range the guess again

    def valid_number(self,number_in_range):     #if convetble to int and in range
        try:
            number_in_range=int(number_in_range)  
        except:
            print("you guesses an invalid number")
            return False
        return self.min<=number_in_range<=self.max
    
    def play(self):  
        print('welcome..')
        while True:
            valid_guess=self.guess() #return only the valid guess and for every valid and invalid guess no of guesses increase
            if valid_guess<self.number:print('your guess was lower')    
            elif valid_guess>self.number:print('your guess was higher')
            else:
                print('you have guessed in {} guesses great!'.format(self.guesses))
                self.play() if 's'==input('enter s') else exit()


g1=Guess_game(50) #we can have different number and diff rage 
g1.play()






#its working fine till few inputs but suddely its showing an error 
# D:\PYTHON\PYCHARM\number_guess_game\venv\Scripts\python.exe D:/PYTHON/PYCHARM/number_guess_game/venv/Include/Guess_game.py
# welcome..
# guess..(0-100)1
# your guess was lower
# guess..(0-100)12
# your guess was lower
# guess..(0-100)32
# your guess was lower
# guess..(0-100)55
# your guess was higher
# guess..(0-100)54
# your guess was higher
# guess..(0-100)123
# your guess is invalid..guess again
# guess..(0-100)45
# Traceback (most recent call last):
#   File "D:/PYTHON/PYCHARM/number_guess_game/venv/Include/Guess_game.py", line 35, in <module>
#     g1.play()
#   File "D:/PYTHON/PYCHARM/number_guess_game/venv/Include/Guess_game.py", line 27, in play
#     if valid_guess<self.number:print('your guess was lower')
# TypeError: '<' not supported between instances of 'NoneType' and 'int'

# Process finished with exit code 1
