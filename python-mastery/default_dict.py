from collections import defaultdict
a,b=map(int,input().split())
d=defaultdict(list)
for i in range(1,a+1):
    d[input()].append(i)
for j in range(1,b+1):
    key=input()
    if len(d[key])!=0:
        print(*d[key])
    else:
        print(-1)


# 5 2
# a
# defaultdict(<class 'list'>, {'a': [1]})
# a
# defaultdict(<class 'list'>, {'a': [1, 2]})
# b
# defaultdict(<class 'list'>, {'a': [1, 2], 'b': [3]})
# a
# defaultdict(<class 'list'>, {'a': [1, 2, 4], 'b': [3]})
# d
# defaultdict(<class 'list'>, {'a': [1, 2, 4], 'b': [3], 'd': [5]})
# d
# 5
# a
# 1 2 4