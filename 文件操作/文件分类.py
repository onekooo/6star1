import os
import shutil
#文件操作
path = 'files'
if not os.path.exists(path):
    print('路径不存在')
    exit()

file_list = os.listdir('files')
os.chdir('files')
for file_name in file_list:
    index = file_name.rfind('.')
    if index == -1:
        print(f'{file_name}没有扩展名')
        continue
    kzm = file_name[index+1:]
    # print(kzm)
    # if kzm not in os.listdir('.'):
    if not os.path.exists(kzm):
        os.mkdir(kzm)
    shutil.move(file_name, kzm)