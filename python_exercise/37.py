import zipfile
import shutil
import os
import time
import glob

directory = ['file/','files/']
for dir in directory:
    if os.path.exists(dir):
        for txtfile in os.listdir(dir):
            os.unlink(dir+txtfile)
        os.rmdir("/Users/vibodapa/Desktop/Ciscoapps/python/python_exercise/"+dir)

time.sleep(1)

zip_object = zipfile.ZipFile("files.zip", "r")
zip_object.extractall('file')

shutil.unpack_archive("files.zip", "files", 'zip')

# shutil.rmtree("/Users/vibodapa/Desktop/Ciscoapps/python/python_exercise/file/")

files = glob.glob("files/*")

for dir in directory:
    count = 0
    if os.path.exists(dir):
        for txtfile in os.listdir(dir):
            file_name, file_extension = os.path.splitext(txtfile)
            if file_extension == ".py":
                count +=1
    print(f"Numer of py files in {dir} are {count}")



file_list=glob.glob1("files","*.py")
print(len(file_list))





