import csv

data = open('example.csv', encoding='utf-8')

csv_data = csv.reader(data)
data_lines = list(csv_data)
# print(data_lines)
all_emails = []
full_names = []
for line in data_lines[1:]:
    print(line)
    all_emails.append(line[3])
    full_names.append(line[1] + " " + line[2])
print(all_emails)
print(full_names)

file_to_output = open('to_save_file.csv', mode='w', newline='')
csv_writer = csv.writer(file_to_output, delimiter=',')
csv_writer.writerow(['a', 'b', 'c'])
csv_writer.writerows([['1','2','3'],['4','5','6']])
file_to_output.close()


