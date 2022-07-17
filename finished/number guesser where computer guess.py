import random

score = 0

for i in range(0, 10):
    guess = int(input('Type a number from 1 to 10: '))
    num = random.randrange(0, 10)

    if num == guess:
        print('computer got it right!')
        print(score)
    else:
        print('Computer got it Wrong!')
        score += 1
        print(score, num)
