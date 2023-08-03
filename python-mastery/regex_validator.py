# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = int(input())
for _ in range(n):
    pattern = input()
    try:
        re.compile(pattern)
        print(True)
    except Exception as e:
        print(False)
