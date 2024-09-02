#quiz

print('welcome to my game ')
answer = input('do you want to play a game(yes/no)').lower()

if answer=='yes':
    print('in the game there are total 5 questions,each question contain 1 mark')
    score=0
    answer=input('what is full form CPU').lower()
    if answer=='central processing unit':
        print('correct')
        score+=1
    else:
        print('incorrect')
    
    answer = input('what is full form of RAM').lower()
    if answer == 'random access meomery':
        print('correct')
        score += 1
    else:
        print('incorrect')
    
    answer = input('what is full form of LOL').lower()
    if answer == 'laugh out loud':
        print('correct')
        score += 1
    else:
        print('incorrect')
    
    answer = input('who is the goat of cricket').lower()
    if answer == 'virat kohli':
        print('correct')
        score += 1
    else:
        print('incorrect')
    
    answer = input('who is the goat of football').lower()
    if answer == 'cristiano ronaldo':
        print('correct')
        score += 1
    else:
        print('incorrect')

    print(f'you score : {score}  marks')

else:
    print('please play the game')




