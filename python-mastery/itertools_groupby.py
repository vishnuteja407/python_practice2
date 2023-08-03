from itertools import groupby

s = input()

data = [(len(list(g)), *[int(k) if k.isdigit() else k]) for k, g in groupby(s)]

print(*data)


# 1222311

# abbcdd

# 122 3 211