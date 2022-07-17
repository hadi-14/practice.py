ids = {}

# give keys and values
keys = ['danishumer1@gmail.com', 'ahmedraza2@gmail.com', 'abdullahalvi3@gmail.com', 'hamzaahmed4@gmail.com', 'farazabbas5@gmail.com', 'zainbabur6@gmail.com', 'harisali7@gmail.com', 'sarimzahid8@gmail.com', 'bilalarshad9@gmail.com']
values = ['Danishumer1', 'Ahmedraza2', 'Abdullahalvi3', 'Hamzaahmed4', 'Farazabbas5', 'Zainbabur6', 'Harisali7', 'Sarimzahid8', 'Bilalasrshad9']

if len(keys) == len(values):
    for i in range(len(keys)):
        ids[keys[i]] = values[i]
        if i == len(keys) - 1:
            print(ids)
else:
    print('number of elements does not match.')
