import re
s = input()

def result(s):
    ss = re.search('[a-zA-Z0-9]+',s)[0]
    result=-1
    for i in range(len(ss)-1):
        if ss[i]==ss[i+1]:
            return ss[i]
    return result

print(result(s))



# ..12345678910111213141516171820212223

# data = input()
# for i, j in zip(data, data[1:]):
#     if i == j and j.isalnum():
#         print(j)
#         break
# else:
#     print(-1)


# re.match() searches for matches from the beginning of a string while 
# re.search() searches for matches anywhere in the string.
# >>> import re
# >>> m = re.match(r'(\w+)@(\w+)\.(\w+)','username@hackerrank.com')
# >>> m.group(0)       # The entire match 
# 'username@hackerrank.com'
# >>> m.group(1)       # The first parenthesized subgroup.
# 'username'
# >>> m.group(2)       # The second parenthesized subgroup.
# 'hackerrank'
# >>> m.group(3)       # The third parenthesized subgroup.
# 'com'
# >>> m.group(1,2,3)   # Multiple arguments give us a tuple.
# ('username', 'hackerrank', 'com')

# >>> import re
# >>> m = re.match(r'(\w+)@(\w+)\.(\w+)','username@hackerrank.com')
# >>> m.groups()
# ('username', 'hackerrank', 'com')

# >>> m = re.match(r'(?P<user>\w+)@(?P<website>\w+)\.(?P<extension>\w+)','myname@hackerrank.com')
# >>> m.groupdict()
# {'website': 'hackerrank', 'user': 'myname', 'extension': 'com'}