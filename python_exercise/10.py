import string
with open("words.txt", "w") as f_write:
    for letter in string.ascii_letters:
        f_write.writelines(letter+"\n")
