# building tic tac toe AI

import random

loc1 = loc2 = loc3 = loc4 = loc5 = loc6 = loc7 = loc8 = loc9 = ' '

value1 = 'X'
value2 = 'O'

true = True
turn1 = True
turn2 = True

print(loc1, '|', loc2, '|', loc3)
print(loc4, '|', loc5, '|', loc6)
print(loc7, '|', loc8, '|', loc9)

while True:

    if true:

        player1 = int(input('Player 1 You/re X Enter Location: '))

        if player1 == 1:
            if loc1 == ' ':
                loc1 = 'X'
            else:
                print('Invalid position')
                continue
        elif player1 == 2:
            if loc2 == ' ':
                loc2 = 'X'
            else:
                print('Invalid position')
                continue
        elif player1 == 3:
            if loc3 == ' ':
                loc3 = 'X'
            else:
                print('Invalid position')
                continue
            if loc1 == loc2 == loc3 or loc3 == loc5 == loc7 or loc3 == loc6 == loc9:
                print('Player 1 win')
        elif player1 == 4:
            if loc4 == ' ':
                loc4 = 'X'
            else:
                print('Invalid position')
                continue
        elif player1 == 5:
            if loc5 == ' ':
                loc5 = 'X'
            else:
                print('Invalid position')
                continue
        elif player1 == 6:
            if loc6 == ' ':
                loc6 = 'X'
            else:
                print('Invalid position')
                continue
        elif player1 == 7:
            if loc7 == ' ':
                loc7 = 'X'
            else:
                print('Invalid position')
                continue
        elif player1 == 8:
            if loc8 == ' ':
                loc8 = 'X'
            else:
                print('Invalid position')
                continue
        else:
            if loc9 == ' ':
                loc9 = 'X'
            else:
                print('Invalid position')
                continue

        print(loc1, '|', loc2, '|', loc3)
        print(loc4, '|', loc5, '|', loc6)
        print(loc7, '|', loc8, '|', loc9)

        value = 'X'

        if loc1 == loc2 == loc3 == value or loc4 == loc5 == loc6 == value or loc7 == loc8 == loc9 == value or loc1 == loc4 == loc7 == value or loc2 == loc5 == loc8 == value or loc3 == loc6 == loc9 == value or loc1 == loc5 == loc9 == value or loc3 == loc5 == loc9 == value:
            print('Player 1 win')
            break

    true = False

    if turn1:
        if loc1 == value1 or loc3 == value1 or loc7 == value1 or loc9 == value1:
            loc5 = value2
        else:
            loc1 = value2
        turn1 = False
    elif turn2:
        if loc5 == value2:
            if loc1 == loc7 == value1:
                loc4 = value2
            elif loc1 == loc3 == value1:
                loc2 = value2
            elif loc9 == loc3 == value1:
                loc6 = value2
            elif loc9 == loc7 == value1:
                loc8 = value2
        elif loc5 != value2:
            if loc2 == value2:
                loc7 = value1
            else:
                loc3 = value1
        else:
            if loc1 == loc2 == value1:
                loc3 = value2
            elif loc4 == loc5 == value1
            elif loc7 == loc8 == loc9 == value or loc1 == loc4 == loc7 == value or loc2 == loc5 == loc8 == value or loc3 == loc6 == loc9 == value or loc1 == loc5 == loc9 == value or loc3 == loc5 == loc9 == value:

        turn2 = False

    print(loc1, '|', loc2, '|', loc3)
    print(loc4, '|', loc5, '|', loc6)
    print(loc7, '|', loc8, '|', loc9)

    value = 'O'

    if loc1 == loc2 == loc3 == value or loc4 == loc5 == loc6 == value or loc7 == loc8 == loc9 == value or loc1 == loc4 == loc7 == value or loc2 == loc5 == loc8 == value or loc3 == loc6 == loc9 == value or loc1 == loc5 == loc9 == value or loc3 == loc5 == loc9 == value:
        print('Player 2 win.')
        break
    else:
        true = True
