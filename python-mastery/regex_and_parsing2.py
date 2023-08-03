import re

s = input()
vowels = "aeiou"
consonants = "qwrtypsdfghjklzxcvbnm"

occurs = re.findall(fr'(?<=[{consonants}])[{vowels}]{{2,}}(?=[{consonants}])', s, re.IGNORECASE)
print(occurs)

print('\n'.join(occurs) if occurs else -1)

# rabcdeefgyYhFjkIoomnpOeorteeeeet


# >>> import re
# >>> re.findall(r'\w','http://www.hackerrank.com/')
# ['h', 't', 't', 'p', 'w', 'w', 'w', 'h', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k', 'c', 'o', 'm']
# >>> import re
# >>> re.finditer(r'\w','http://www.hackerrank.com/')
# <callable-iterator object at 0x0266C790>
# >>> map(lambda x: x.group(),re.finditer(r'\w','http://www.hackerrank.com/'))
# ['h', 't', 't', 'p', 'w', 'w', 'w', 'h', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k', 'c', 'o', 'm']