# from itertools import groupby, islice

# list1 = [1,2,3,4,6,7,9,11,12,15,16,17,19]

# list2 = []

# for i in range(len(list1)):
#     list2.append(list1[i]-i)


# print(list2)

# data = [(len(list(g)), k) for k, g in groupby(list2)]

# print(data)
# my_iterator = iter(list1)
# for j,_ in data:
#     print("-".join(list(map(str, islice(my_iterator, j)))))




from itertools import chain
 
li = ['123', '456', '789']
 
res = list(chain.from_iterable(li))
 
print("res =", res, end ="\n\n")
 
new_res = list(map(int, res))
 
print("new_res =", new_res)
 
sum_of_li = sum(new_res)
 
print("\nsum =", sum_of_li)



from itertools import chain
 
# some consonants
consonants = ['d', 'f', 'k', 'l', 'n', 'p']
 
# some vowels
vowels = ['a', 'e', 'i', 'o', 'u']
 
# resultatnt list
res = list(chain(consonants, vowels))
 
# sorting the list
res.sort()
 
print(res)


from itertools import chain
 
li = ['ABC', 'DEF', 'GHI', 'JKL']
 
# using chain-single iterable.
res1 = list(chain(li))
 
 
res2 = list(chain.from_iterable(li))
 
print("using chain :", res1, end ="\n\n")
 
print("using chain.from_iterable :", res2)