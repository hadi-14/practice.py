
original_list = ['1', '2', '3', '4', '5', '4', '4', '3', '2', '6', '4', '2', '3', '4', '5', '6', '7', '8', '9', '6', '5']
new_list = []
duplicates = 0

for i in original_list:
    if i in new_list:
        duplicates += 1
    else:
        new_list.append(i)

print('new list:', new_list)
print('duplicates removed:', duplicates)