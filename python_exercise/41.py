# with open("user_data.txt", 'a+') as data:
#     while True:
#         input_string = input("Please enter a string: ")
#         if input_string == 'CLOSE':
#             break
#         else:
#             data.write(input_string+"\n")


file = open("user_data.txt", 'a+')

while True:
    input_string = input("Please enter a string: ")
    if input_string == 'CLOSE':
        file.close()
        break
    elif input_string == 'SAVE':
        file.close()
        file = open("user_data.txt", 'a+')
    else:
        file.write(input_string+"\n")