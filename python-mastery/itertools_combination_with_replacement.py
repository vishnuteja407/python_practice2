from itertools import combinations_with_replacement
s, k = input().split()

myarray = list(map(lambda x: "".join(x), combinations_with_replacement(sorted(s.upper(), key=str), int(k))))
for ele in myarray:
    if ele == '':
        continue
    print(ele)
