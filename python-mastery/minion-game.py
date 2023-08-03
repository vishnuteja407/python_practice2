from itertools import combinations
x = "BANANA"
stuart, kevin = 0, 0

possible_sub_strings = [''.join(l) for i in range(len(x)) for l in combinations(x, i+1)]
possible_sub_strings = list(set(possible_sub_strings))
print(possible_sub_strings)

for sub_string in possible_sub_strings:
    if x.find(sub_string) != -1:
        print(sub_string)
        points = x.count(sub_string)
        if sub_string[0] in 'AEIOU':
            kevin += points
            print("Kevin Points",kevin)
        else:
            stuart += points
            print("Stuart Points", stuart)

if kevin == stuart:
    print('Draw')
elif kevin > stuart:
    print(f'Kevin {kevin}')
else:
    print(f'Stuart {stuart}')



# def minion_game(string):
#     stuart, kevin = 0, 0
#     for i, ch in enumerate(string):
#         points = len(string)-i
#         print(points)
#         if ch in 'AEIOU':
#             kevin += points
#             print("Kevin Points",kevin)
#         else:
#             stuart +=points
#             print("Stuart Points", stuart)
            
#     if kevin == stuart:
#         print('Draw')
#     elif kevin > stuart:
#         print(f'Kevin {kevin}')
#     else:
#         print(f'Stuart {stuart}')

# if __name__ == '__main__':
#     s = input()
#     minion_game(s)