# a = [1, 2, 3]
# for index, value in enumerate(a):
#     print(f'Item {value} has index {index}')


# import time
# condition_1 = True
# n = 0
# while condition_1:
#     print("Hello") 
#     n+=1
#     if n == 3:
#         print("End of Loop")
#         break
#     time.sleep(n)


# while True:
#     print("Hello")

#     if 2 > 1:
#         pass

#     print("Hi")

# d = dict(weather = "clima", earth = "terra", rain = "chuva") 

# input_value = input("Enter a word: ")

# if input_value in d.keys():
#     print(f"{d[input_value]}")
# else:
#     print("Invalid word")


d = dict(weather = "clima", earth = "terra", rain = "chuva")
def vocabulary(word):
    try:
        return d[word]
    except Exception as e:
        print(e.__class__)
        print("That word doesn't exist!") 
     
word = input("Enter word: ").lower()
print(vocabulary(word))

    