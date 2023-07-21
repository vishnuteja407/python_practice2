# key = [ele for ele in range(1, 31)]
# d = {"a": key[:10], "b": key[10:20], "c": key[20:30]}
# print(d)

from pprint import pprint
     
d = {"a":list(range(1, 11)), "b":list(range(11, 21)), "c":list(range(21, 31))}
pprint(d)

print(d['b'][2])

for key, value in d.items():
    print(f"{key} has value {value}")
