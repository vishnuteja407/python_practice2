#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    ar2 = []
    count = 0
    for ele in ar:
        if ele not in ar2:
            ar2.append(ele)
    print(ar2)
    for ele in ar2:
        val = ar.count(ele)
        # print(val)
        if val > 1:
            count += math.floor(val/2)
    return count


# # Method 1 Using Library collections
# from collections import Counter
# def sockMerchant(n, ar):
#     pair = 0
#     for i in list(Counter(ar).values()):
#         pair += (i//2)
#     return pair
    
# # Method 2 Using set
# def sockMerchant(n, ar):
#     pair = 0
#     for i in set(ar) :
#         pair += ar.count(i)//2
#     return pair

# # Method 3 Using loop 
# def sockMerchant(n, ar):   
#     ar.sort()
#     Count = 1
#     pair = 0
#     for i in range(1,n) :
#         if ar[i] == ar[i-1] :
#             Count += 1
#         else :
#             pair += Count//2
#             Count = 1
        
#         if i == n-1 and ar[i] == ar[-2] :
#             pair += Count//2

#     return pair

if __name__ == '__main__':
    fptr = open('Data/sales_by_match.txt', 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

# 8
# [10, 20, 30, 40, 10, 20, 50, 10]