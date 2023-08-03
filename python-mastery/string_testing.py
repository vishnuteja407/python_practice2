# def print_full_name(first, last):
#     # Write your code here
#     result = f"Hello {first} {last}! You just delved into python."
#     print(result)

# if __name__ == '__main__':
#     first_name = input()
#     last_name = input()
#     print_full_name(first_name, last_name)



# def count_substring(string, sub_string):
#     count = 0
#     for i in range(len(string)):
#         if string[i:i+len(sub_string)] == sub_string:
#             count +=1
#     return count

# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()
    
#     count = count_substring(string, sub_string)
#     print(count)



# if __name__ == '__main__':
#     s = input()
#     for cmd in ["alnum","alpha","digit","lower","upper"]:
#         exec(f"print(any(c.is{cmd}() for c in s))")

#     f_any = lambda method: any([method(ch) for ch in s])
#     print(f_any(str.isalnum), f_any(str.isalpha), f_any(str.isdigit), f_any(str.islower), f_any(str.isupper), sep = '\n')


# if __name__ == '__main__':
#     s = input()
#     functions = ["isalnum", "isalpha", "isdigit", "islower", "isupper"]
#     for f in functions:
#         print(any(eval(f"c.{f}()") for c in s))

# if __name__ == '__main__':
#     s = input()
#     for cmd in ["alnum","alpha","digit","lower","upper"]:
#         exec(f"print(any(c.is{cmd}() for c in s))")



# n = int(input("Enter number of rows in odd sequence:"))
# char = "H"
# special_char = ' '
# # top cone
# for i in range(1, n*2+1, 2):
#     print((char * i).center(n*2, special_char))

# #below cone
# for i in range(1, n+2):
#     print((special_char+char*n).ljust(i, special_char), (special_char*(n*2)+char*n).rjust(i, special_char))

# #middle
# for i in range(1, n+2):
#     print((special_char+char*(n*5)).ljust(i, special_char))

# #above reverse cone
# for i in range(1, n+2):
#     print((special_char+char*n).ljust(i, special_char), (special_char*(n*2)+char*n).rjust(i, special_char))

# # bottom right cone
# for i in range(n*2-1, 0, -2):
#     print((special_char*n*3)+(char * i).center(n*2, special_char))



thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))