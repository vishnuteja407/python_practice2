#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

# Method 1
# def countingValleys(steps, path):
#     valley = 0
#     S = 0
#     for i in path :
#         if i == "U" :
#             S += 1
#             if S == 0 :
#                 valley += 1
#         else :
#             S -= 1
#     print(valley)
#     return valley

# Method 2
def countingValleys(steps, path):
    high = []
    S = 0
    for i in path :
        if i == "U" :
            S += 1
            high.append(S)
        else :
            S -= 1
            high.append(S)
    for i in range(steps) :
        if high[i] == 0 and high[i-1] < 0 :
            S += 1
    return S




if __name__ == '__main__':
    fptr = open('Data/counting_valleys.txt', 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()



# 8
# UDDDUDUU