print("guess a number between ('1-100)")
guesses=0
while True:
    try:
        guess=int(input('guess nuber'))
    except:
        print('its invalid guess again')
        continue
    if guess <50:print("guess was under")
    elif guess >51:print("guess was over")
    else:print("you guessed it in {} guesses".format(guesses))
    guesses+=1

