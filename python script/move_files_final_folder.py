import shutil
import os

base_dir = r"./data-obj"
some_dir = r'./images1'
some_dir1 = r'./annotation1'
for files in os.listdir(some_dir):
        file = os.path.join(some_dir, files)
        shutil.move(file, base_dir)
        
for files in os.listdir(some_dir1):
        file = os.path.join(some_dir1, files)
        shutil.move(file, base_dir)