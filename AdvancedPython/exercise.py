import shutil
import os
import re

shutil.unpack_archive("unzip_me_for_instructions.zip","instructions", 'zip')

# f = open("instructions/extracted_content/instructions.txt", "r")
# f.readlines()
# f.close()

file_path = "instructions/extracted_content/"
for folders, sub_folders, files in os.walk(file_path):
    # print(f"Folders: {folders}")
    # print("\n")
    for file in files:
        filename = folders+'/'+file
        # print(filename)
        with open(filename, 'r') as f_read:
            data = f_read.readlines()
            for line in data:
                match = re.findall(r"\d{3}-\d{3}-\d{3}", line)
                if match:
                    print(filename)
                    print(match)
            
