import os
import shutil
#write the name of the directory here
#that needs to get sorted
#path
path = input ("Enter the name of the directory to be sorted: ")

list_of_files = os.listdir(path)
for file in list_of_files:
    name,ext = os.path.splitext(file)

#this is going to store the extension type
    ext = ext[1:]
    if ext =='':
        continue
    if os.path.exist(path+'/'+ext):
        shutil.move(path+'/'+file, path+ '/'+ext+'/'+file)