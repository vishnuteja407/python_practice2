# import random
# characters = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
# password = "".join(random.sample(characters, 6))

# check = True


# while check:
#     password = input("Enter the password: ")
#     if len(password) > 5 and any(ele.isupper() for ele in password) and any(ele.isdigit() for ele in password):
#         check = False
#         print(password)
#     else:
#         print("Password is not fine")




while True:
    notes = []
    psw = input("Enter password: ")
    if not any(i.isdigit() for i in psw):
        notes.append("You need at least one number")
    if not any(i.isupper() for i in psw):
        notes.append("You need at least one uppercase letter")
    if len(psw) < 5:
        notes.append("You need at least 5 characters")
    if len(notes) == 0:
        print("Password is fine")
        break
    else:
        print("Please check the following: ")
        for note in notes:
            print(note)      
