# f = open("fileone.txt", "w+")
# f.write("One file")
# f.close()

# f = open("filetwo.txt", "w+")
# f.write("two file")
# f.close()

import zipfile
import time

comp_file = zipfile.ZipFile("comp_file.zip", "w")
comp_file.write("fileone.txt", compress_type=zipfile.ZIP_DEFLATED)
comp_file.write("filetwo.txt", compress_type=zipfile.ZIP_DEFLATED)
comp_file.close()

zip_object = zipfile.ZipFile("comp_file.zip", "r")
zip_object.extractall('extracted_content')

# time.sleep(10)
# import os

# os.unlink("/Users/vibodapa/Desktop/Ciscoapps/python/AdvancedPython/extracted_content/fileone.txt")
# os.unlink("/Users/vibodapa/Desktop/Ciscoapps/python/AdvancedPython/extracted_content/filetwo.txt")
# os.rmdir("/Users/vibodapa/Desktop/Ciscoapps/python/AdvancedPython/extracted_content")

import shutil
filepath = "/Users/vibodapa/Desktop/Ciscoapps/python/AdvancedPython/extracted_content"
output_filename = "example"
shutil.make_archive(output_filename, 'zip', filepath)

shutil.unpack_archive("example.zip", "final_unzip", 'zip')

