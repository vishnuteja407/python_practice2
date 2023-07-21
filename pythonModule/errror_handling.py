# for i in ['a','b','c']:
#     try:
#         print(i**2)
#     except TypeError:
#         print("Invalid integer value")

# x = 5
# y = 0

# try:
#     z = x / y
# except Exception as e:
#     print(e.__class__)
# finally:
#     print("All Done")

def ask():
    while True:
        try:
            num = int(input("Please enter a interger value: "))
            result = num ** 2
        except:
            print(" Invalid Input value")
            continue
        else:
            print("Square done")
            print(result)
            break

ask()
