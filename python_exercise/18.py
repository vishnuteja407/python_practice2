import os
arr = []
word = "python"

directory = 'letters/'

for txtfile in os.listdir(directory):
    with open(directory+txtfile, 'r') as f_data:
        letter = f_data.read()
    if letter in word:
        arr.append(letter)

arr.sort()
print(arr)