#!/bin/python3

import math
import os
import random
import re
import sys


# res = [''.join(sorted(ele)) for ele in test_list]

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#
# possible substring from given string
# s = "abcd"
# res = [s[i: j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)]

from collections import Counter

# def sherlockAndAnagrams(s):
#     combs2 = lambda x: x * (x - 1) // 2
#     print(combs2)
#     key = lambda i, j: tuple(sorted(s[j: j + i + 1]))
#     print(key)
#     subs = Counter(
#         key(i, j) for i in range(len(s) - 1) for j in range(len(s) - i)
#     )
#     print(dict(subs))
#     return sum(map(combs2, subs.values()))

def sherlockAndAnagrams(s):
    res = [s[i: j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)]
    res = list(map(lambda x:"".join(sorted(x)), res))
    print(res)
    vals = dict(Counter(res))
    count = {k:v for k, v in vals.items() if v >= 2}
    return len(count)
    


if __name__ == '__main__':
    fptr = open("Data/sherlock_anagrams.txt", 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)
        print(result)

        fptr.write(str(result) + '\n')

    fptr.close()

# 2
# abba
# abcd
# 1
# cdcd