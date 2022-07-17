mylist = []

YN = False

while True:
    inpt = input('Enter: ')
    if inpt.lower() == 'stop' or inpt.lower() == 'stop!' or inpt.lower() == 'finish':
        print('final list:',mylist)
        break
    elif inpt.lower() == 'delete':
        del mylist[len(mylist)-1]
        print(mylist)
    elif inpt.lower().startswith('delete') and inpt.endswith(')'):
        tf = False
        output = ''
        for i in inpt:
            if i == ')':
                tf = False
            elif tf:
                output += i
            elif i == '(':
                tf = True
        mylist.remove(output)
        print(mylist)
    elif 'help' in inpt.lower() or 'instruction' in inpt.lower() or inpt.lower() == 'what to do?':
        print('1: enter elements to add into the list')
        print('2: enter stop to stop creating list')
        print('3: enter delete to delete the last element')
        print('4: enter delete({what to delete}) to delete the entered element')
        print('5: enter integers to change to enter integers')
        print('6: enter strings to change to normal or strings mode')
        print('7: enter {number} + { int}  to give onetime number')
    elif inpt.lower() == 'integers' or inpt.lower() == 'numbers':
        YN = True
        print('Changed to ' + inpt + ' mode')
    elif inpt.lower() == 'strings' or inpt.lower() == 'alphabets':
        YN = False
        print('Changed to ' + inpt + ' mode')
    elif YN:
        try:
            mylist.append(int(inpt))
            print(mylist)
        except:
            print('The input contains alphabets')
    elif inpt.lower().endswith('int'):
        num = ''
        for i in inpt:
            try:
                i = int(i)
            except:
                i = str(i)
            if i in range(10):
                num += str(i)
            elif i == ' ':
                mylist.append(int(num))
                print(mylist)
    else:
        mylist.append(inpt)
        print(mylist)
