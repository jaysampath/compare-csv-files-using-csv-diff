import os as os
from zipfile import ZipFile

source_files_path="C:/path/zip-files"
destination= "C:/path/zipped/zipped.zip"

files_to_zipped = os.listdir(source_files_path)

num_files_zipped = 0
with ZipFile(destination,'w') as zip:
        # writing each file one by one
        for file in files_to_zipped:
            file_to_be_zipped = source_files_path + "/" + file
            zip.write(file_to_be_zipped)
            num_files_zipped = num_files_zipped + 1
            print('Added to zip', file_to_be_zipped)
        print("Zipped", num_files_zipped, "files and added to", destination)

