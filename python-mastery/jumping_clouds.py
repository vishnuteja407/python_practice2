#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    i  = 0
    index = 0
    while index != len(c)-1:
        try:
            if c[index+2] == 0:
                index += 2
                i += 1
            else:
                index += 1
                i +=1
        except Exception as e:
            index += 1
            i +=1
    return i

if __name__ == '__main__':
    fptr = open("Data/jumping_clouds.py", 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)
    print (result)

    fptr.write(str(result) + '\n')

    fptr.close()


# 6
# 0 0 0 1 0 0