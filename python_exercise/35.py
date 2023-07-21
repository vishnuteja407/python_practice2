import sqlite3
import pandas
import csv

conn = sqlite3.connect('database.db')

curr = conn.cursor()
columns = "Rank,Country,Area,Population"+"\n"

curr.execute("SELECT * FROM countries WHERE area >= 2000000")
rows = curr.fetchall()

conn.close()

# with open("country_info.csv", 'w') as data:
#     data.write(columns)
#     for row in rows:
#         for x in row:
#             data.write(str(x)+",")
#         data.write("\n")



# df = pandas.DataFrame.from_records(rows)
# df.columns = ["Rank", "Country", "Area", "Population"]
# df.to_csv("country_info.csv", index=False) 


fields = ["Rank", "Country", "Area", "Population"]
with open("country_info.csv", 'w') as data:
    # creating a csv writer object 
    csvwriter = csv.writer(data) 
        
    # writing the fields 
    csvwriter.writerow(fields) 
        
    # writing the data rows 
    csvwriter.writerows(rows)
    

