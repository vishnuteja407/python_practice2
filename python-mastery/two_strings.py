#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoStrings' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def twoStrings(s1, s2):
    for s in s1:
        if s in s2:
            return "Yes"
    return "No"

if __name__ == '__main__':
    fptr = open("Data/two_strings.txt", 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)
        print(result)

        fptr.write(result + '\n')

    fptr.close()


# 2
# hello
# world

# hi
# world