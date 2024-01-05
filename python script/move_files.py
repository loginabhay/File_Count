import shutil
import os

img_dir = r"./images"
ano_dir = r"./annotation"
some_dir = r'./images1'
some_dir1 = r'./annotation1'

for fold in os.listdir(img_dir):
    folder = os.path.join(img_dir, fold)
    for files in os.listdir(folder):
        file = os.path.join(folder, files)
        shutil.copy(file, some_dir)
        
for fold in os.listdir(ano_dir):
    folder = os.path.join(ano_dir, fold)
    for files in os.listdir(folder):
        file = os.path.join(folder, files)
        shutil.copy(file, some_dir1)