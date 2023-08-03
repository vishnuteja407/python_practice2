import csv

f = open('Data/portfolio.csv','r')

f_csv = csv.reader(f)

headers = next(f_csv)

print(headers)

rows = list(f_csv)
# print(rows)

# for row in rows:
#     print (row)

# for name, shares, price in rows:
#     print(name, shares, price)

# for name, _, price in rows:
#     print(name, price)

from collections import defaultdict

byname = defaultdict(list)
for name, *data in rows:
    byname[name].append(data)
# print(byname)
print(byname['IBM'])

for share, price in byname['IBM']:
    print(share, price)

row = rows[0]

for col, val in zip(headers, row):
    print(col, val, sep=", ")

for row in rows:
    record  = dict(zip(headers, row))
    print(record)

# Generator Expressions
nums = [1,2,3,4,5]
squares = (x*x for x in nums)

print(next(squares))

for x in squares:
    print(x)

