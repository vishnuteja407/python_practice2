import math
import os
import random
import re
import sys
from collections import Counter


def company_logo(s):
    dict1 = Counter(s)
    # print(**dict1.most_common(3))
    # dict2 = sorted(dict1.items(), key=lambda i: i[0])
    # print(dict2)
    for i in dict1.most_common(3):
        print(*i)
   



if __name__ == '__main__':
    s = sorted(input())
    company_logo(s)


# qwertyuiopasdfghjklzxcvbnm
# a 1
# b 1
# c 1