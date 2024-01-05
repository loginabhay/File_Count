import os
import random
import shutil

base_dir = './data-obj'

imgs = []
train = 0.8

for files in os.listdir(base_dir):
    file = os.path.join(base_dir, files)
    file_abs = os.path.abspath(file)
    file_name = os.path.basename(file)
    if file_name.endswith('.jpeg'):
        imgs.append(file_abs)

train_imgs = random.sample(imgs, int(len(imgs) * train))
test_imgs = list(set(imgs) - set(train_imgs))


with open('train.txt', 'w') as f:
    for line in train_imgs:
        f.write(line + '\n')
        print(line)

print('---------------Done--------------------')
print('[INFO] Train.txt created!!!!')


with open('test.txt', 'w') as f:
    for line in test_imgs:
        f.write(line + '\n')
        print(line)

print('---------------Done--------------------')
print('[INFO] Test.txt created!!!!')
