from itertools import combinations

s,k = input().split()
for i in range(int(k)+1):
    myarray = list(map(lambda x: "".join(x), combinations(sorted(s.upper(), key=str), i)))
    for ele in myarray:
        if ele == '':
            continue
        print(ele)


# HACK 2

# >>> from itertools import combinations
# >>> 
# >>> print list(combinations('12345',2))
# [('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '4'), ('3', '5'), ('4', '5')]
# >>> 
# >>> A = [1,1,3,3,3]
# >>> print list(combinations(A,4))
# [(1, 1, 3, 3), (1, 1, 3, 3), (1, 1, 3, 3), (1, 3, 3, 3), (1, 3, 3, 3)]