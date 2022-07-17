import random
import time

name = input('What is your name?')
print("Hello " + name + ".")
ages: str = input("How old are you?")
age = int(ages)
while age not in range(0, 121):
    list = ["You cheeky", "You cheater", "Man don't try to hack"]
    print(random.choice(list))
    print("try again! It's not possible")
    time.sleep(1)
    ages: str = input("How old are you?")
    age = int(ages)
heal: str = input("How are you?")
health = heal.lower()
while True:
    if health == "fine" or "good" or "well" or "all right" or "very well" or "very good" or "nice" or "feeling good" or "feeling right" or "gorgeous" or "not fine" or "bad" or "not in a good health" or "not in a good state" or "very bad" or "worrying" or "felling bad" or "don't ask" or "don't worry":
        break
    print("Try again")
    heal: str = input("How are you?")
    health = heal.lower()
if health == "fine" or "good" or "well" or "all right" or "very well" or "very good" or "nice" or "feeling good" or "feeling right" or "gorgeous":
    mylist = ["ok", "Good", "very well", "I am happy for you", "I hope you stay fine", "gorgeous"]
    print(random.choice(mylist))
elif health == "not fine" or "bad" or "not in a good health" or "not in a good state" or "very bad" or "worrying" or "felling bad":
    worry: str = input("What Happened to you?")
    mylist = ["I hope yo get good soon", "Hope your condition gets better", "I wish you were fine", "I am quite sad 😞",
              "I can't do anything but I can pray"]
    print(random.choice(mylist))
elif health == "don't ask" or "don't worry":
    mylist = ["ok", "Sorry", "My bad 😂 ", "sorry,My bad 😂 ", "I Don't care"]
    print(random.choice(mylist))
if age in range(5, 12):
    a: str = input("Want to have a test?")
    test: str = a.lower()
    marks = 0
    i = True
    while True:
        if test == "yes" or "yup" or "ya man" or "you not it yes" or "i think so" or "ok" or "be quick" or "yes,be quick" or "sure" or "ok what you say so" or "ok,what you say":
            i = True
            break
        elif test == "no" or "nope" or "no thanks" or "no need" or "no requirement" or "not required" or "not at all":
            list = ["ok", "no problem", "Means you don't need it"]
            print(random.choice(list))
            i = False
            break
        print("try again!")
        a: str = input("Want to have a test?")
        test: str = a.lower()
    while i:
        more: str = input("Which test?")
        mores = more.lower()
        marks = 0
        while mores == "subtraction" or "sub" or "-" or "minus" or "multiplication" or "multiply" or "*" or "division" or "divide" or "/" or "addition" or "add" or "sum" or "+":
            if mores == "subtraction" or "sub" or "-" or "minus" or "multiplication" or "multiply" or "*" or "division" or "divide" or "/" or "addition" or "add" or "sum" or "+":
                break
            print("Error: Type international word or symbol")
            more: str = input("Which test?")
            mores = more.lower()
        for y in range(1, 11):
            if mores == "multiplication" or "multiply" or "*":
                num1 = int(random.randrange(2, 11))
                num2 = int(random.randrange(2, 11))
                text2 = "{} x {} = ?"
                answers = input(text2.format(num1, num2))
                answer = int(answers)
                num3 = num1 * num2
                if answer == num3:
                    print("You were right.")
                    marks = marks + 1
                elif answer != num3:
                    print("You were wrong")
                    print(num3)
            elif mores == "division" or "divide" or "/":
                num1 = int(random.randrange(2, 11))
                num2 = int(random.randrange(2, 11))
                text1 = "{} / {} = ?"
                answer = input(text1.format(num1, num2))
                num3 = num1 / num2
                if answer == num3:
                    print("You were right.")
                    marks = marks + 1
                elif answer != num3:
                    print("You were wrong")
                    print(num3)
            elif mores == "addition" or "add" or "sum" or "+":
                num1 = int(random.randrange(100, 9999))
                num2 = int(random.randrange(100, 9999))
                text3 = "{} + {} = ?"
                answer = input(text3.format(num1, num2))
                num3 = num1 + num2
                if answer == num3:
                    print("You were right.")
                    marks = marks + 1
                elif answer != num3:
                    print("You were wrong")
                    print(num3)
            elif mores == "subtraction" or "sub" or "-" or "minus":
                num1 = int(random.randrange(100, 9999))
                num2 = int(random.randrange(100, 9999))
                text4 = "{} - {} = ?"
                answer = input(text4.format(num1, num2))
                num3 = num1 - num2
                if answer == num3:
                    print("You were right.")
                    marks = marks + 1
                elif answer != num3:
                    print("You were wrong")
                    print(num3)
            text = "{}/{}"
            print(text.format(marks, y))
        cont: str = input("Want to continue?")
        con = cont.lower()
        while True:
            if con == "ok" or "yes" or "sure" or "all right" or "yup" or "well, ok" or "i would like to" or "my pleasure" or "it would be my pleasure" or "no" or "not at all" or "nope" or "i don't want to" or "no more" or "never":
                break
            print("Try again")
            cont: str = input("Want to continue?")
            con = cont.lower()
        if con == "ok" or "yes" or "sure" or "all right" or "yup" or "well, ok" or "i would like to" or "my pleasure" or "it would be my pleasure":
            choice = ["ok", "good", "well, ok", "fine", "done", "alright"]
            print(random.choice(choice))
            more: str = input("Which test?")
            marks = 0
        elif con == "no" or "not at all" or "nope" or "i don't want to" or "no more" or "never":
            print("ok")
            break
