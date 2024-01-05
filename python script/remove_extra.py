import os

some_dir = r'./images1'
some_dir1 = r'./annotation1'
count = 0
for files in os.listdir(some_dir):
    f = os.path.basename(files)
    count +=1
    file = f.split('.')
    file[0] = file[0] +'.txt'
    if file[0] not in os.listdir(some_dir1):
        os.remove(os.path.join(some_dir,files))
    if count % 1000 == 0:
        print('{} files completed !!'.format(count))