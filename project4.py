#stone paper

import random
print('welcome to game')
user_wins = 0
computer_wins = 0
tie = 0

options = ['rock','paper','scissors']

while True:
    user_input = input('Type rock/paper/scissors or q to quit: ').lower()
    if user_input == 'q':
        break

    if user_input not in options:
        continue

    random_number = random.randint(0,2)
    #rock:0 ,paper:1 , scissors:2
    computer_picks = options[random_number]
    print('computer picked',computer_picks + '.')

    if user_input == computer_picks:
        print('match tie')
        tie+=1

    elif user_input == 'rock' and computer_picks == 'scissors':
        print('you won')
        user_wins +=1
    elif user_input == 'paper' and computer_picks == 'stone':
        print('you won')
        user_wins+=1
    elif user_input == 'scissors' and computer_picks == 'paper':
        print('you won')
        user_wins+=1
    else:
        print('you lost')
        computer_wins+=1

print('you won',user_wins,'times')
print('computer won',computer_wins,'times')
print('match tie',tie,'times')
print('Thank You')