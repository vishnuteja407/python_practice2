
import re
S, k = input(), input()
pat = re.compile(k)
m = pat.search(S)

if m:
    while m:
        print((m.start(), m.end()-1))
        i = m.start() + 1
        m = pat.search(S, i)
else:
    print((-1, -1))


# def find_indexes(a_string, substring):
#     start = 0   

#     indexes = []

#     while start < len(a_string):
        
#         start = a_string.find(substring, start)
#         if start == -1 and len(indexes) == 0:
#             return [(-1, -1)]
#         elif start == -1:
#             return indexes

#         if len(substring) > 1:
#             end = start + 1
#         else:
#             end = start
#         indexes.append((start, end))

#         start += 1

#     return indexes


# string = input()
# print(*find_indexes(string, eval('input()')), sep="\n") 
