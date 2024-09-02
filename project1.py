#Text adventure game
while True:
    answer = input('would you like to play a game?(yes/no) ')

    if answer.lower().strip()=='yes':

        answer=input('welcome to game,you can see three doors chose only one (one /two /three)').lower().strip()
        if answer == 'one':
            answer=input('you chose right path,you are safe,which vehicle you want to drive to go home(car/bike)').lower().strip()

            if answer=='car':
                print('you are now driving mustang,drive safe ')
            else:
                print('you are now driving bike,wear helmet and drive safe')


        elif answer=='two':
            answer=input('you are now in hell would you like to fight with monster (yes/no)').lower().strip()

            if answer=='yes':
                print('that is not good idea,you lose because you are cat')

            else:
                print('good choice')

        elif answer=='three':
            answer=input('you are now became marvel,would you like to be a spiderman(yes/no').lower().strip()

            if answer=='yes':
                print('good choice')
            else:
                print('you are not  marvel fan')

    else:
        print('please play the game please ')
        break
