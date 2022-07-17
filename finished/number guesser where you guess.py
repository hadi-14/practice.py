import random

score = 0

for i in range(0, 10):
    guess = int(input('Guess a number from 1 to 10: '))
    num = random.randrange(0, 10)

    if guess == num:
        print('You got it right!')
        score += 1
        print(score)
    else:
        print('Wrong')
        print(score, num)
