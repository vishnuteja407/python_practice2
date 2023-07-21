import collections

mylist = [1,2,3,4,5,3,1,1,2,3,4,1,1,2,3,4,5,6]

print(collections.Counter(mylist))

letters = "aaaabbbbbcccccddddddaaa"

c = collections.Counter(letters)
print(c)
print(c.most_common(2))
print(list(c))

d = collections.defaultdict(lambda: 0)
d['correct'] = 100
print(d)
print(d[1])

Dog = collections.namedtuple("Dog",['age', 'breed', 'name'])
sammy = Dog(age=5, breed='Husky', name='Sam')
print(type(sammy))
print(sammy)