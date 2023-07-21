import shutil
import glob
import os

shutil.unpack_archive("subdirs.zip", "subdirs", 'zip')

# files = glob.glob1("subdirs", "*.py")

count = 0
for dir, subdir, files in os.walk("subdirs"):
    if files:
        for file in files:
            file_name, file_extension = os.path.splitext(file)
            if file_extension == ".py":
                count += 1

print(f"Number of py files are {count}")

file_list = glob.glob("subdirs/**/*.py", recursive=True)
print(len(file_list))