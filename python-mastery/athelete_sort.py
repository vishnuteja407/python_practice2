import math
import os
import random
import re
import sys

def athelete_sort(arr, k):
    data = sorted(arr, key=lambda x:x[k])
    return data


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input().strip())
    result = athelete_sort(arr, k)
    for i in result:
        print(*i)






# 5 3
# 10 2 5
# 7 1 0
# 9 9 9
# 1 23 12
# 6 5 9
# 1