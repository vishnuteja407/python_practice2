data = input("Enter the value separated by comma: ")

split_data = data.split(",")

with open("save_values.txt", "a") as data:
    for string in split_data:
        data.write(string +"\n")