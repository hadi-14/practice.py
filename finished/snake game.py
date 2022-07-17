import random

score = 0
empty = '□'
snake = '■'
food = '▣'


def out():
    print(f'{loc1} {loc2} {loc3} {loc4} {loc5}')
    print(f'{loc6} {loc7} {loc8} {loc9} {loc10}')
    print(f'{loc11} {loc12} {loc13} {loc14} {loc15}')
    print(f'{loc16} {loc17} {loc18} {loc19} {loc20}')
    print(f'{loc21} {loc22} {loc23} {loc24} {loc25}')


loc1 = loc2 = loc3 = loc4 = loc5 = loc6 = loc7 = loc8 = loc9 = loc10 = loc11 = loc12 = loc13 = loc14 = loc15 = loc16 = loc17 = loc18 = loc19 = loc20 = loc21 = loc22 = loc23 = loc24 = loc25 = empty

rand = random.randrange(1, 26)

if rand == 1:
    loc1 = snake
elif rand == 2:
    loc2 = snake
elif rand == 3:
    loc3 = snake
elif rand == 4:
    loc4 = snake
elif rand == 5:
    loc5 = snake
elif rand == 6:
    loc6 = snake
elif rand == 7:
    loc7 = snake
elif rand == 8:
    loc8 = snake
elif rand == 9:
    loc9 = snake
elif rand == 10:
    loc10 = snake
elif rand == 11:
    loc11 = snake
elif rand == 12:
    loc12 = snake
elif rand == 13:
    loc13 = snake
elif rand == 14:
    loc14 = snake
elif rand == 15:
    loc15 = snake
elif rand == 16:
    loc16 = snake
elif rand == 17:
    loc17 = snake
elif rand == 18:
    loc18 = snake
elif rand == 19:
    loc19 = snake
elif rand == 20:
    loc20 = snake
elif rand == 21:
    loc21 = snake
elif rand == 22:
    loc22 = snake
elif rand == 23:
    loc23 = snake
elif rand == 24:
    loc24 = snake
elif rand == 25:
    loc25 = snake

rand_food = random.randrange(1, 26)

if rand_food == 1:
    loc1 = food
elif rand_food == 2:
    loc2 = food
elif rand_food == 3:
    loc3 = food
elif rand_food == 4:
    loc4 = food
elif rand_food == 5:
    loc5 = food
elif rand_food == 6:
    loc6 = food
elif rand_food == 7:
    loc7 = food
elif rand_food == 8:
    loc8 = food
elif rand_food == 9:
    loc9 = food
elif rand_food == 10:
    loc10 = food
elif rand_food == 11:
    loc11 = food
elif rand_food == 12:
    loc12 = food
elif rand_food == 13:
    loc13 = food
elif rand_food == 14:
    loc14 = food
elif rand_food == 15:
    loc15 = food
elif rand_food == 16:
    loc16 = food
elif rand_food == 17:
    loc17 = food
elif rand_food == 18:
    loc18 = food
elif rand_food == 19:
    loc19 = food
elif rand_food == 20:
    loc20 = food
elif rand_food == 21:
    loc21 = food
elif rand_food == 22:
    loc22 = food
elif rand_food == 23:
    loc23 = food
elif rand_food == 24:
    loc24 = food
elif rand_food == 25:
    loc25 = food

out()

while True:
    move = input('Enter direction:').lower()

    if loc1 == snake:
        if move == 'w':
            loc21 = snake
            rand = 21
            loc1 = empty
        elif move == 'a':
            loc5 = snake
            rand = 5
            loc1 = empty
        elif move == 's':
            loc6 = snake
            rand = 6
            loc1 = empty
        elif move == 'd':
            loc2 = snake
            rand = 2
            loc1 = empty
    elif loc2 == snake:
        if move == 'w':
            loc22 = snake
            rand = 22
            loc2 = empty
        elif move == 'a':
            loc1 = snake
            rand = 1
            loc2 = empty
        elif move == 's':
            loc7 = snake
            rand = 7
            loc2 = empty
        elif move == 'd':
            loc3 = snake
            rand = 3
            loc2 = empty
    elif loc3 == snake:
        if move == 'w':
            loc23 = snake
            rand = 23
            loc3 = empty
        elif move == 'a':
            loc2 = snake
            rand = 2
            loc3 = empty
        elif move == 's':
            loc8 = snake
            rand = 8
            loc3 = empty
        elif move == 'd':
            loc4 = snake
            rand = 4
            loc3 = empty
    elif loc4 == snake:
        if move == 'w':
            loc24 = snake
            rand = 24
            loc4 = empty
        elif move == 'a':
            loc3 = snake
            rand = 3
            loc4 = empty
        elif move == 's':
            loc9 = snake
            rand = 9
            loc4 = empty
        elif move == 'd':
            loc5 = snake
            rand = 5
            loc4 = empty
    elif loc5 == snake:
        if move == 'w':
            loc25 = snake
            rand = 25
            loc5 = empty
        elif move == 'a':
            loc4 = snake
            rand = 4
            loc5 = empty
        elif move == 's':
            loc10 = snake
            rand = 10
            loc5 = empty
        elif move == 'd':
            loc1 = snake
            rand = 1
            loc5 = empty
    elif loc6 == snake:
        if move == 'w':
            loc1 = snake
            rand = 1
            loc6 = empty
        elif move == 'a':
            loc10 = snake
            rand = 10
            loc6 = empty
        elif move == 's':
            loc11 = snake
            rand = 11
            loc6 = empty
        elif move == 'd':
            loc7 = snake
            rand = 7
            loc6 = empty
    elif loc7 == snake:
        if move == 'w':
            loc2 = snake
            rand = 2
            loc7 = empty
        elif move == 'a':
            loc6 = snake
            rand = 6
            loc7 = empty
        elif move == 's':
            loc12 = snake
            rand = 12
            loc7 = empty
        elif move == 'd':
            loc8 = snake
            rand = 8
            loc7 = empty
    elif loc8 == snake:
        if move == 'w':
            loc3 = snake
            rand = 3
            loc8 = empty
        elif move == 'a':
            loc7 = snake
            rand = 7
            loc8 = empty
        elif move == 's':
            loc13 = snake
            rand = 13
            loc8 = empty
        elif move == 'd':
            loc9 = snake
            rand = 9
            loc8 = empty
    elif loc9 == snake:
        if move == 'w':
            loc4 = snake
            rand = 4
            loc9 = empty
        elif move == 'a':
            loc8 = snake
            rand = 8
            loc9 = empty
        elif move == 's':
            loc14 = snake
            rand = 14
            loc9 = empty
        elif move == 'd':
            loc10 = snake
            rand = 10
            loc9 = empty
    elif loc10 == snake:
        if move == 'w':
            loc5 = snake
            rand = 5
            loc10 = empty
        elif move == 'a':
            loc9 = snake
            rand = 9
            loc10 = empty
        elif move == 's':
            loc15 = snake
            rand = 15
            loc10 = empty
        elif move == 'd':
            loc6 = snake
            rand = 6
            loc10 = empty
    elif loc11 == snake:
        if move == 'w':
            loc6 = snake
            rand = 6
            loc11 = empty
        elif move == 'a':
            loc15 = snake
            rand = 15
            loc11 = empty
        elif move == 's':
            loc16 = snake
            rand = 16
            loc11 = empty
        elif move == 'd':
            loc12 = snake
            rand = 12
            loc11 = empty
    elif loc12 == snake:
        if move == 'w':
            loc7 = snake
            rand = 7
            loc12 = empty
        elif move == 'a':
            loc11 = snake
            rand = 11
            loc12 = empty
        elif move == 's':
            loc17 = snake
            rand = 17
            loc12 = empty
        elif move == 'd':
            loc13 = snake
            rand = 13
            loc12 = empty
    elif loc13 == snake:
        if move == 'w':
            loc8 = snake
            rand = 8
            loc13 = empty
        elif move == 'a':
            loc12 = snake
            rand = 12
            loc13 = empty
        elif move == 's':
            loc18 = snake
            rand = 18
            loc13 = empty
        elif move == 'd':
            loc14 = snake
            rand = 14
            loc13 = empty
    elif loc14 == snake:
        if move == 'w':
            loc9 = snake
            rand = 9
            loc14 = empty
        elif move == 'a':
            loc13 = snake
            rand = 13
            loc14 = empty
        elif move == 's':
            loc19 = snake
            rand = 19
            loc14 = empty
        elif move == 'd':
            loc15 = snake
            rand = 15
            loc14 = empty
    elif loc15 == snake:
        if move == 'w':
            loc10 = snake
            rand = 10
            loc15 = empty
        elif move == 'a':
            loc14 = snake
            rand = 14
            loc15 = empty
        elif move == 's':
            loc20 = snake
            rand = 20
            loc15 = empty
        elif move == 'd':
            loc11 = snake
            rand = 11
            loc15 = empty
    elif loc16 == snake:
        if move == 'w':
            loc11 = snake
            rand = 11
            loc16 = empty
        elif move == 'a':
            loc20 = snake
            rand = 20
            loc16 = empty
        elif move == 's':
            loc21 = snake
            rand = 21
            loc16 = empty
        elif move == 'd':
            loc17 = snake
            rand = 17
            loc16 = empty
    elif loc17 == snake:
        if move == 'w':
            loc12 = snake
            rand = 12
            loc17 = empty
        elif move == 'a':
            loc16 = snake
            rand = 16
            loc17 = empty
        elif move == 's':
            loc22 = snake
            rand = 22
            loc17 = empty
        elif move == 'd':
            loc18 = snake
            rand = 18
            loc17 = empty
    elif loc18 == snake:
        if move == 'w':
            loc13 = snake
            rand = 13
            loc18 = empty
        elif move == 'a':
            loc17 = snake
            rand = 17
            loc18 = empty
        elif move == 's':
            loc23 = snake
            rand = 23
            loc18 = empty
        elif move == 'd':
            loc19 = snake
            rand = 19
            loc18 = empty
    elif loc19 == snake:
        if move == 'w':
            loc14 = snake
            rand = 14
            loc19 = empty
        elif move == 'a':
            loc18 = snake
            rand = 2018
            loc19 = empty
        elif move == 's':
            loc24 = snake
            rand = 24
            loc19 = empty
        elif move == 'd':
            loc20 = snake
            rand = 20
            loc19 = empty
    elif loc20 == snake:
        if move == 'w':
            loc15 = snake
            rand = 15
            loc20 = empty
        elif move == 'a':
            loc19 = snake
            rand = 19
            loc20 = empty
        elif move == 's':
            loc25 = snake
            rand = 25
            loc20 = empty
        elif move == 'd':
            loc16 = snake
            rand = 16
            loc20 = empty
    elif loc21 == snake:
        if move == 'w':
            loc16 = snake
            rand = 16
            loc21 = empty
        elif move == 'a':
            loc25 = snake
            rand = 25
            loc21 = empty
        elif move == 's':
            loc1 = snake
            rand = 1
            loc21 = empty
        elif move == 'd':
            loc22 = snake
            rand = 22
            loc21 = empty
    elif loc22 == snake:
        if move == 'w':
            loc17 = snake
            rand = 17
            loc22 = empty
        elif move == 'a':
            loc21 = snake
            rand = 21
            loc22 = empty
        elif move == 's':
            loc2 = snake
            rand = 2
            loc22 = empty
        elif move == 'd':
            loc23 = snake
            rand = 23
            loc22 = empty
    elif loc23 == snake:
        if move == 'w':
            loc18 = snake
            rand = 18
            loc23 = empty
        elif move == 'a':
            loc22 = snake
            rand = 22
            loc23 = empty
        elif move == 's':
            loc3 = snake
            rand = 3
            loc23 = empty
        elif move == 'd':
            loc24 = snake
            rand = 24
            loc23 = empty
    elif loc24 == snake:
        if move == 'w':
            loc19 = snake
            rand = 19
            loc24 = empty
        elif move == 'a':
            loc23 = snake
            rand = 23
            loc24 = empty
        elif move == 's':
            loc4 = snake
            rand = 4
            loc24 = empty
        elif move == 'd':
            loc25 = snake
            rand = 25
            loc24 = empty
    elif loc25 == snake:
        if move == 'w':
            loc20 = snake
            rand = 20
            loc25 = empty
        elif move == 'a':
            loc24 = snake
            rand = 24
            loc25 = empty
        elif move == 's':
            loc5 = snake
            rand = 5
            loc25 = empty
        elif move == 'd':
            loc21 = snake
            rand = 21
            loc25 = empty

    if rand_food == rand:
        score += 1
        print(score)
        if score == 10:
            print('You Win!')
            break

        rand_food = random.randrange(1, 26)

        if rand_food == 1:
            loc1 = food
        elif rand_food == 2:
            loc2 = food
        elif rand_food == 3:
            loc3 = food
        elif rand_food == 4:
            loc4 = food
        elif rand_food == 5:
            loc5 = food
        elif rand_food == 6:
            loc6 = food
        elif rand_food == 7:
            loc7 = food
        elif rand_food == 8:
            loc8 = food
        elif rand_food == 9:
            loc9 = food
        elif rand_food == 10:
            loc10 = food
        elif rand_food == 11:
            loc11 = food
        elif rand_food == 12:
            loc12 = food
        elif rand_food == 13:
            loc13 = food
        elif rand_food == 14:
            loc14 = food
        elif rand_food == 15:
            loc15 = food
        elif rand_food == 16:
            loc16 = food
        elif rand_food == 17:
            loc17 = food
        elif rand_food == 18:
            loc18 = food
        elif rand_food == 19:
            loc19 = food
        elif rand_food == 20:
            loc20 = food
        elif rand_food == 21:
            loc21 = food
        elif rand_food == 22:
            loc22 = food
        elif rand_food == 23:
            loc23 = food
        elif rand_food == 24:
            loc24 = food
        elif rand_food == 25:
            loc25 = food

    out()
