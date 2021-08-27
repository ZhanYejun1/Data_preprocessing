# 对所有格式文件重命名

import os
path = r"C:\Users\A3\Desktop\新建文件夹"
path_list = os.listdir(path)
i = 30
for index in path_list:
    os.rename(path+'/'+index, path+'/'+str(i).zfill(4)+index[-4:])
    i = i + 1