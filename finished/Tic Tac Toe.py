loc1 = loc2 = loc3 = loc4 = loc5 = loc6 = loc7 = loc8 = loc9 = ' '

true = True

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

    player2 = int(input('player 2 You/re O Enter Location: '))

    if player2 == 1:
        if loc1 == ' ':
            loc1 = 'O'
        else:
            print('Invalid position')
            continue
    elif player2 == 2:
        if loc2 == ' ':
            loc2 = 'O'
        else:
            print('Invalid position')
            continue
    elif player2 == 3:
        if loc3 == ' ':
            loc3 = 'O'
        else:
            print('Invalid position')
            continue
    elif player2 == 4:
        if loc4 == ' ':
            loc4 = 'O'
        else:
            print('Invalid position')
            continue
    elif player2 == 5:
        if loc5 == ' ':
            loc5 = 'O'
        else:
            print('Invalid position')
            continue
    elif player2 == 6:
        if loc6 == ' ':
            loc6 = 'O'
        else:
            print('Invalid position')
            continue
    elif player2 == 7:
        if loc7 == ' ':
            loc7 = 'O'
        else:
            print('Invalid position')
            continue
    elif player2 == 8:
        if loc8 == ' ':
            loc8 = 'O'
        else:
            print('Invalid position')
            continue
    else:
        if loc9 == ' ':
            loc9 = 'O'
        else:
            print('Invalid position')
            continue

    print(loc1, '|', loc2, '|', loc3)
    print(loc4, '|', loc5, '|', loc6)
    print(loc7, '|', loc8, '|', loc9)

    value = 'O'

    if loc1 == loc2 == loc3 == value or loc4 == loc5 == loc6 == value or loc7 == loc8 == loc9 == value or loc1 == loc4 == loc7 == value or loc2 == loc5 == loc8 == value or loc3 == loc6 == loc9 == value or loc1 == loc5 == loc9 == value or loc3 == loc5 == loc9 == value:
        print('Player 2 win.')
        break
    else:
        true = True
