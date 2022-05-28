import os
# shutil:module that does high level commands i.e copying
import shutil
source = input("Enter source folder name: ")
dest = input("Enter dest folder name: ")
source = source+ "/"
dest = dest+"/"
list_of_files = os.listdir(source)
for file in list_of_files:
    # .move() move files (to different folders)
    shutil.move((source+file), dest)