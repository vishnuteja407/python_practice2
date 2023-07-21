import string

# letter_arr = []
# for letter in string.ascii_lowercase:
#     letter_arr.append(letter)
# letter_arr1 = letter_arr[::2]
# letter_arr2 = letter_arr[1::2]
# with open('letter.txt', 'w') as f_write: 
#     for i, j in zip(letter_arr1, letter_arr2):
#         f_write.write(i+j+"\n")

with open("letter.txt", "w") as f_write:
    for i, j in zip(string.ascii_uppercase[0::2], string.ascii_uppercase[1::2]):
        f_write.write(i + j + "\n")