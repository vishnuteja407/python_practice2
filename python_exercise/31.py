with open("countries_raw.txt", "r") as data:
    unfiltered_data = data.readlines()



unfiltered_data = [country.strip("\n") for country in unfiltered_data]

countries = [country for country in unfiltered_data if len(country)> 1 and country != 'Top of Page']
# print(countries)
with open("countries.txt", 'w') as data:
    for country in countries:
        data.write(country+"\n")