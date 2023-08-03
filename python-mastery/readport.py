import csv
from operator import le

# def read_portfolio(filename):
#     portfolio = []
#     with open(filename, "r") as f:
#         rows = csv.reader(f)
#         header = next(rows)
#         for row in rows:
#             record = {
#                 'name' : row[0],
#                 'shares' : int(row[1]),
#                 'price' : float(row[2])
#             }
#             portfolio.append(record)
#     return portfolio


# portfolio = read_portfolio('Data/portfolio.csv')
# from pprint import pprint
# pprint(portfolio)

# Find all holdings more than 100 shares
# [s for s in portfolio if s['shares'] > 100]
# [{'name': 'CAT', 'shares': 150, 'price': 83.44}, 
#  {'name': 'MSFT', 'shares': 200, 'price': 51.23}]

# Compute total cost (shares * price)
# sum([s['shares']*s['price'] for s in portfolio])
# 44671.15


# Find all unique stock names (set)
# { s['name'] for s in portfolio }
# {'MSFT', 'IBM', 'AA', 'GE', 'CAT'}


# Count the total shares of each of stock
# totals = { s['name']: 0 for s in portfolio }
# print(totals)
# for s in portfolio:
#     totals[s['name']] += s['shares']
# print(totals)


# {'AA': 100, 'IBM': 150, 'CAT': 150, 'MSFT': 250, 'GE': 95}

# from collections import Counter
# totals = Counter()
# for s in portfolio:
#     totals[s['name']] += s['shares']

# print(totals)
# print(totals.most_common(2))

# from collections import defaultdict
# byname = defaultdict(list)
# for s in portfolio:
#     byname[s['name']].append(s)

# print(byname)
# print(byname['IBM'])
# print(byname['AA'])


import reader
portfolio = reader.read_csv_as_dicts('Data/portfolio.csv', [str,int,float])

for s in portfolio:
    print(s)

rows = reader.read_csv_as_dicts('Data/ctabus.csv', [str,str,str,int])
print(len(rows))



