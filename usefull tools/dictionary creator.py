warn = input('do you want to get warnings for key being replaced? ')

dictionary = {}

YN = False

while True:
    try:
        old_key = keys
    except:
        old_key = '1'
    keys = input('Enter key: ')
    new_key = keys
    if keys in dictionary.keys() and warn.lower() == 'yes':
        print('you are replacing a key')
        if input('Are you sure?').lower() == 'no':
            continue
    elif keys.lower() == 'stop' or keys.lower() == 'stop!' or keys.lower() == 'finish':
        print('final dictionary:', dictionary)
        break
    elif keys.lower() == 'delete':
        try:
            del dictionary[old_key]
        except:
            print('not possible enter key')
        print(dictionary)
        continue
    elif keys.lower().startswith('delete') and keys.endswith(')'):
        tf = False
        output = ''
        for i in keys:
            if i == ')':
                tf = False
            elif tf:
                output += i
            elif i == '(':
                tf = True
        del dictionary[output]
        print(dictionary)
        continue
    elif 'help' in keys.lower() or 'instruction' in keys.lower() or keys.lower() == 'what to do?':
        print('1: enter elements to add into the list')
        print('2: enter stop to stop creating list')
        print('3: enter delete to delete the last element')
        print('4: enter delete({what to delete}) to delete the entered element')
        print('5: enter integers to change to enter integers')
        print('6: enter strings to change to normal or strings mode')
        print('7: enter {number} + { int}  to give onetime number')
        continue
    elif keys.lower() == 'integers' or keys.lower() == 'numbers':
        YN = True
        print('Changed to ' + keys + ' mode')
        continue
    elif keys.lower() == 'strings' or keys.lower() == 'alphabets':
        YN = False
        print('Changed to ' + keys + ' mode')
        continue
    elif YN:
        try:
            new_key = int(keys)
        except:
            print('The input contains alphabets')
            continue
    elif keys.lower().endswith('int'):
        num = ''
        for i in keys:
            try:
                i = int(i)
            except:
                i = str(i)
            if i in range(10):
                num += str(i)
            elif i == ' ':
                new_key = int(num)
    elif keys.lower() == 'printable form':
        print('Keys', ':', 'Values')
        for x, y in dictionary.items():
            print(x, ':', y)

    while True:

        try:
            old_value = values
        except:
            old_value = '1'

        values = input('Enter value: ')

        if values.lower() == 'integers' or values.lower() == 'numbers':
            YN = True
            print('Changed to ' + values + ' mode')
            continue
        elif values.lower() == 'strings' or values.lower() == 'alphabets':
            YN = False
            print('Changed to ' + values + ' mode')
            continue
        elif YN:
            try:
                new_value = int(values)
                break
            except:
                print('The input contains alphabets')
                continue
        elif values.lower().endswith('int'):
            num = ''
            for i in values:
                try:
                    i = int(i)
                except:
                    i = str(i)
                if i in range(10):
                    num += str(i)
                elif i == ' ':
                    new_value = int(num)
                    break
        else:
            new_value = values
            break

    dictionary[new_key] = new_value
    print(dictionary)
