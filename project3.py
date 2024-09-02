#number guessing

import random

range = input('type a number between you want to guess: ')

if range.isdigit():
    range=int(range)

    if range <= 0:
        print('please try number greater than zero')
        quit()
else:
    print('please type a number greater than zero')
    quit()

random_number = random.randint(0,range) #it contain 0 and the range
guesses = 0

while True:
    guesses += 1
    user_guess = input('guess any number: ')
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('please type a number greater than zero')
        quit()
        continue

    if user_guess == random_number:
        print('you got it')
        break
    elif user_guess > random_number:
        print('you are above the number')
    else:
        print('you are below the number')

print('you got it in', guesses,'guesses')
