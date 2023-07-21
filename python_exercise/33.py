# checklist = ["Portugal", "Germany", "Munster", "Spain"]

# with open("countries.txt", "r") as countries:
#     countries_list = [country.strip("\n") for country in countries.readlines()]
    
# for place in checklist:
#     if place not in countries_list:
#         checklist.remove(place)

# print(checklist)

import re


check_list = ['Portugal', 'Germany', 'Spain']
revised_list = [i+"\n" for i in check_list]

with open("countries_missing.txt", "r") as countries:
    countries_list = countries.readlines()

complete_list = sorted(countries_list + revised_list)

with open("countries_full_list.txt", 'w') as revised_data:
    for data in complete_list:
        revised_data.write(data)