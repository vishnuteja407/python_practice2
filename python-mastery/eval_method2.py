CMD = input()
if "print" in CMD :
    eval(CMD)
else :
    print(eval(CMD))

# print(2 + 3)


# print(exec(input()))

# >>> eval("9 + 5")
# 14
# >>> x = 2
# >>> eval("x + 3")
# 5

# >>> type(eval("len"))
# <type 'builtin_function_or_method'>