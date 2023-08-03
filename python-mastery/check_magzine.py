#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#

# def checkMagazine(magazine, note):
#     for word in note:
#         if word in magazine:
#             magazine.remove(word) 
#             note[note.index(word)] = 0       
#             if set(note) == {0}:
#                 print("Yes")
#         else:
#             print("No")

def checkMagazine(magazine, note):
    for n in note:
        try:
            magazine.remove(n)
        except:
            print("No")
            return
        
    print("Yes")

# def checkMagazine(magazine, note):
#     mag = magazine
#     wordsInMag = True
#     for word in note:
#         try:
#             mag.remove(word)
#         except:
#             print("No")
#             wordsInMag = False
#             break
#     if(wordsInMag):
#         print("Yes")


        


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)



# 6 5     
# two times three is not four
# two times two is four
