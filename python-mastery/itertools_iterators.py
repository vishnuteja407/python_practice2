from itertools import combinations

n = int(input())
line = input().split()
k = int(input())

groups = list(combinations(line, k))
print(groups)
a_count = sum('a' in group for group in groups)

probability = a_count / len(groups)
print(f'{probability:.12f}')

# 10
# b b a b b b b b b b
# 10


# 4
# a a c d
# 2