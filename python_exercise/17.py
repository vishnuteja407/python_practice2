import os
arr = []

for txtfile in os.listdir("letters"):
    with open("letters/"+txtfile, 'r') as f_data:
        arr.append(f_data.read())

arr.sort()
print(arr)


# solution2

import glob

letters = []

file_list = glob.glob("letters/*.txt")
print(file_list)

for filename in file_list:
    with open(filename, 'r') as data:
        letters.append(data.read())

print(letters)

# for folders, files, subfolders in os.walk("/Users/vibodapa/Desktop/Ciscoapps/python/python_exercise"):
#     print(folders)
#     print(files)
#     print(subfolders)
