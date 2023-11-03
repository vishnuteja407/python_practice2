import glob
import os

file_path = "/Users/vibodapa/Documents/BPA-3.2.2/AS-BAC-BPA/tests/giza"

service = "BRMSC_v1.4.0"

if os.path.exists(file_path):
    os.chdir(file_path)

for dirpath, dirs, files in os.walk(os.getcwd()): 
    for dir in dirs:     
        if dir == service:
            # print(dirpath)
            if dirpath.find("components") != -1:
                scripts_path = glob.glob(dirpath+"/"+service+"/*/*/*.robot", recursive=True)
                for files in scripts_path:
                    print(files.split("giza/")[1])
            elif dirpath.find("UI") != -1 or dirpath.find("end-to-end") != -1:
                scripts_path = glob.glob(dirpath+"/"+service+"/*/*.robot", recursive=True)
                for file in scripts_path:
                    print(file.split("giza/")[1])

           