#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    total_occurences = s.count('a') * (n//len(s))
    total_occurences = total_occurences + s[0:n%len(s)].count('a')
    
    return total_occurences
    

if __name__ == '__main__':
    fptr = open("Data/repeated_string.py", 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)
    print(result)

    fptr.write(str(result) + '\n')

    fptr.close()



# ababaqaq
# 7