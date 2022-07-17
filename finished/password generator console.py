# password generator

import random

number = int(input('Enter the number of Password: '))
length = int(input('Enter the length of the password: '))

for x in range(0, number):
    password = ''
    for y in range(0, length):
        password += random.choice(
            ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z', '!', '#', '$', '%', '&', "'", '"', '(', ')', '*', '+', ',', '-', '.', '/', ':',
             ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
    print(password)