def gensquares(n):
    for num in range(n):
        yield num*num

for x in gensquares(10):
    print(x)

import random
def rand_num(low, high, n):
    for i in range(n):
        yield random.randint(low, high)

for num in rand_num(1, 10, 12):
    print(num)

s = "hello"
iter_s = iter(s)
print(next(iter_s))
print(next(iter_s))
print(next(iter_s))
print(next(iter_s))
print(next(iter_s))