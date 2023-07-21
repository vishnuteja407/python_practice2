import csv

with open('Exercise_Files/find_the_link.csv') as data:
    csv_data = csv.reader(data)
    data_lines = list(csv_data)
    # print(data_lines)
    url = ''
    position = 0
    # for i in range(len(data_lines)):
    #     url += data_lines[i][position]
    #     position += 1
    for row_num, data in enumerate(data_lines):
        url += data[row_num]
print(url)

   