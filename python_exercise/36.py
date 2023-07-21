import sqlite3
import pandas

conn = sqlite3.connect('database.db')

cursor = conn.cursor()

# Preparing SQL queries to INSERT a record into the database.
# with open("ten_more_countries.txt", "r") as country_missing:
#     for country in country_missing:
#         country_list = [ele.strip("\n") for ele in country.split(",")]
#         print(country_list)
#         print(country_list[1])
#         cursor.execute("INSERT INTO countries VALUES (NULL, ?, ?, NULL)", (country_list[1], country_list[2]))

data = pandas.read_csv("ten_more_countries.txt")
for index, row in data.iterrows():
    cursor.execute("INSERT INTO countries VALUES (NULL, ?, ?, NULL)", (row[1], row[2]))


# cursor.execute("DELETE from countries where population=NULL")
conn.commit()

cursor.execute("SELECT * FROM countries")
rows = cursor.fetchall()
print(rows)

conn.close()

