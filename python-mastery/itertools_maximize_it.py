

# n, percent  = input().split()
# list1 = []
# for i in range(int(n)):
#     data = list(map(int, input().split()))
#     list1.append(max(data))

# sum = sum(map(lambda x: x*x, list1))
# print(sum)
# print(sum%int(percent))




import itertools

if '__main__' in __name__:
    k, m = map(int, input().split())
    
    l = []
    for _ in range(k):
        l2 = list(map(int, input().split()))[1:]
        l.append(l2)
        
    s = []
    for p in itertools.product(*l):
        s.append(sum([pow(i, 2, m) for i in p]) % m)
print(s)
print(max(s))


# 3 1000
# 2 5 4
# 3 7 8 9 
# 5 5 7 8 9 10 


# 5 84
# 1 765952241
# 3 289380515 265118103 309882974
# 2 747649220 587740446
# 2 682866882 596381508
# 1 342723101