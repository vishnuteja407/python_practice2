import readrides
import datetime
rows = readrides.read_rides_as_dicts('Data/ctabus.csv')
routes = set({})
# print(rows[0])

#How many bus routes exist in Chicago?
for row in rows:
    routes.add(row['route'])

# print(len(routes))

#How many people rode the number 22 bus on February 2, 2011? What about any route on any date of your choosing?
def people_boarded(day, route):
    date = datetime.datetime.strptime(day, "%B %d, %Y")
    date = f'{date:%m/%d/%Y}'
    for row in rows:
        if row['date'] == date and row['route'] == route:
            return row['rides']

# print(people_boarded("February 2, 2011", "24"))

#What is the total number of rides taken on each bus route?
from collections import Counter
totals = Counter()
for row in rows:
    totals[row['route']] += row['rides']

# print(totals)
#What five bus routes had the greatest increase in ridership?
# print(totals.most_common(5))

from collections import defaultdict
byname = defaultdict(list)
for row in rows:
    byname[row['route']].append(row)

# print(byname['90N'][0]['rides'])
# print(byname['90N'][-1]['rides'])

updated_rows = {}
for route in routes:
    old = byname[route][0]['rides']
    new = byname[route][-1]['rides']
    pc = round((new - old) / abs(old) * 100, 2)
    updated_rows.update({route: pc})

# print(updated_rows)
import itertools

sorted_data = dict(sorted(updated_rows.items(), key=lambda x:x[1], reverse=True))
N = 5

out = dict(itertools.islice(sorted_data.items(), N))

print(out.keys())


routes = { row['route'] for row in rows }
print(len(routes))

routeids = { id(row['route']) for row in rows }
print(len(routeids))

#there are only 181 distinct route names,
# but the resulting list of dictionaries contains 542305 different route strings. 
# Maybe this is something that could be fixed with a bit of caching or object reuse. 
# As it turns out, Python has a function that can be used to cache strings, sys.intern()

# import tracemalloc
# tracemalloc.start()
# from sys import intern
# import reader
# rows = reader.read_csv_as_dicts('Data/ctabus.csv', [intern, str, str, int])
# routeids = { id(row['route']) for row in rows }
# print(len(routeids))

# print(tracemalloc.get_traced_memory())


import tracemalloc
tracemalloc.start()
from sys import intern
import reader
rows = reader.read_csv_as_dicts('Data/ctabus.csv', [intern, intern, str, int])

print(tracemalloc.get_traced_memory())
