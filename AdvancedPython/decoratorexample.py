# def hello():
#     return "Hi Jose!"

# def other(some_func):
#     print("Other code runs here!")
#     print(some_func())

# print(other(hello))

def new_decorator(original_func):
    def wrap_func():
        print("Some extra code before original function")
        original_func()
        print("Some extra code after original function")

    return wrap_func

def func_needs_decorator():
    print("I want to be decaorated!!!")

decorated_func = new_decorator(func_needs_decorator)

decorated_func()

@new_decorator
def func_needs_decorator():
    print("I want to be decaorated!!!")

func_needs_decorator()