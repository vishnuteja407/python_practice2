import glob
import shutil
import os
import csv

fields = ["Hostname"]
line = '''

##################################################################################


'''


line_to_replace = '''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
'''

content_to_append = '''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
show clock
09:40:56.797 GMT Tue Aug 16 2022
deviceName#
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
'''

file_path = "/Users/vibodapa/Desktop/CEWA-DEFECT/"
directory = "files"

csv_name = "devices.csv"

dest = file_path + directory

csv_file = os.path.join(dest, csv_name)
print(csv_file)

data = glob.glob(file_path+"**/*.txt")

if not os.path.exists(dest):
    os.makedirs(dest)

files = glob.glob(os.path.join(dest, '*'))
for file in files:
    if os.path.isfile(file):
        os.remove(file)
print(f"Deleted files in {dest}")

device_array = []
for filename in data:
    print(filename)
    try:
        device_name = filename.split("/")[-1].split("_")[1]
        if device_name not in device_array:
            device_array.append(device_name)
            dest_path = f"{dest}/{device_name}.txt"
            print(dest_path)
            shutil.copy2(filename, dest_path)
                        
    except IndexError:
        pass


for file in glob.glob(os.path.join(dest, '*')):
    file_name = file.split("/")[-1].split(".")[0]
    print(file_name)
    # with open(csv_file, "w") as csv_file:
    #     csv_writer = csv.writer(csv_file)
    #     csv_writer.writerow(fields)
    #     csv_writer.writerow(file_name)

    with open(file, "r") as read_file:
        with open(dest+"/"+file_name+".log", "a+") as write_file:
            data = read_file.read()
            data = data.replace(file_name+" #", "")
            data = data.replace(line, line_to_replace)
            content_to_append = content_to_append.replace("deviceName", file_name)
            write_file.write(content_to_append)
            write_file.write(data)

    content_to_append = content_to_append.replace(file_name, "deviceName")
        

# for file in glob.glob(os.path.join(dest, '*')):
#     if file.endswith(".log"):
#         with open(file, "r") as read_data:
#             data = read_data.readlines()
#             for line in data:
#                 if line.startswith("show") or line.startswith("dir"):
#                     position = data.index(line)
#                     print(position)
#                     data.insert(position+1, line)
#                     print(data)


# with open("/Users/vibodapa/Desktop/CEWA-DEFECT/files/USGAATLSO02VDM0001.log", "r") as read_data:
#     data = read_data.readlines()
#     for line in data:
#         if line.startswith("show") or line.startswith("dir"):
#             print(line)
#             position = data.index(line)
#             print(position)
#             data.insert(position+1, line)
#     print(data)

