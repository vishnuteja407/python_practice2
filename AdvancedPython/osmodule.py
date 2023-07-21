# f = open("pratice.txt", "w+")
# f.write("This is a test string")
# f.close()

import os

# print(os.getcwd())
# print(os.listdir())

# print(os.listdir("/Users/vibodapa/"))

# import shutil
# shutil.move("../MilestoneProject/pratice.txt", os.getcwd())


import send2trash

# send2trash.send2trash('pratice.txt')
file_path = "/Users/vibodapa/Desktop/Ciscoapps/Ansible"
for folder, sub_folder, files in os.walk(file_path):
    print(f"Currently looking at {folder}")
    print("\n")
    print("\t Sub directories are: ")
    for sub_fold in sub_folder:
        print(f"Subfolder: {sub_fold}")
    print("\n")
    print("The files are: ")
    for f in files:
        print(f"\tFile: {f}")
    print("\n")

