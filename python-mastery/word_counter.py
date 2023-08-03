from collections import Counter

n = int(input())
list1 = []
for i in range(n):
    s = input()
    list1.append(s)

word_counter = dict(Counter(list1))
print(len(word_counter))
print(*word_counter.values())

