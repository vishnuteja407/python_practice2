from readport import read_portfolio
portfolio = read_portfolio('Data/portfolio.csv')

print(sum(s['shares'] * s['price'] for s in portfolio))

print(min(s['shares'] for s in portfolio))

print(any(s['name']=='IBM' for s in portfolio))
print(all(s['name']=='IBM' for s in portfolio))

print(sum(s['shares'] for s in portfolio if s['name']=='IBM'))

import tracemalloc
tracemalloc.start()
import readrides

rows = readrides.read_rides_as_dicts('Data/ctabus.csv')
rt22 = [row for row in rows if row['route'] == '22']
print(max(rt22, key=lambda row: row['rides']))
current, peak = tracemalloc.get_traced_memory()
print(current)
print(peak)
tracemalloc.stop()

import tracemalloc
tracemalloc.start()
import csv
f = open('Data/ctabus.csv')
f_csv = csv.reader(f)
headers = next(f_csv)
rows = (dict(zip(headers,row)) for row in f_csv)
rt22 = (row for row in rows if row['route'] == '22')
print(max(rt22, key=lambda row: int(row['rides'])))
current, peak = tracemalloc.get_traced_memory()
print(current)
print(peak)
