def word_counter(word):
    data = word.split(" ")
    result = len(data)
    return result

string = input("Enter the string:  ")
func = word_counter(string)
print(func)

