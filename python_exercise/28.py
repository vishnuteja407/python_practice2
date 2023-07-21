while True:    
    user = input("Enter username: ")
    with open("users.txt", 'r') as f_data:
        data = f_data.readlines()
        user_data = [i.strip("\n") for i in data]

        if user in user_data:
            print("User already exists")
            continue
        else:
            print("User available")
            break



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
        print("Password should meet following requirements ")
        for note in notes:
            print(note) 