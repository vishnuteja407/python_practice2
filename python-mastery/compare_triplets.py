#!/bin/python

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    alice = list(map(lambda x,y: x>y, a, b))
    bob = list(map(lambda x,y: x<y, a, b))
    print(alice)
    print (bob)
if __name__ == '__main__':

    a = map(int, input().rstrip().split())

    b = map(int, input().rstrip().split())

    result = compareTriplets(a, b)
    print(result)

#else if
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# half the even numbers, square the odd numbers, and cube the numbers greater than 5
new_list = [n * n * n if n > 5 else n * n if n % 2 == 0 else n / 2 for n in numbers]

print(new_list)
# [0.5, 4, 1.5, 16, 2.5, 216, 343, 512, 729, 1000]
