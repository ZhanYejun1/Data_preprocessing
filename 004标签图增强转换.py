import cv2
import numpy as np
from PIL import Image
from os import getcwd
import os
import matplotlib.pyplot as plt

import random

random.seed(0)

# 生成图片id并保存在txt中
def train_id(srcimage, saveBasePath):
    train_percent = 1

    temp_img = os.listdir(srcimage)
    total_img = []
    for i in temp_img:
        if i.endswith(".png"):  # 根据srcimage图片名修改  eg. jpg png and so on.
            total_img.append(i)

    num = len(total_img)
    list = range(num)
    tr = int(num * train_percent)
    train = random.sample(list, tr)

    ftrain = open(os.path.join(saveBasePath, 'label_id.txt'), 'w')  # 保存txt文件路径

    for i in list:
        name = total_img[i][:-4] + '\n'
        if i in train:
            ftrain.write(name)

    ftrain.close()

# 生成图片id+格式
def train_txt(srcimage, saveBasePath):
    sets = [('label','format')]

    for year, image_set in sets:
        image_ids = open(saveBasePath + 'label_id.txt')
        list_file = open('%s_%s.txt' % (year, image_set), 'w')
        for image_id in image_ids:
            image_id = image_id.split()[0]
            image_id = str(image_id)
            list_file.write(srcimage + '%s.png' % (image_id))
            list_file.write('\n')
        list_file.close()




def save_img(index):
    with open("label_format.txt") as f:
        lines = f.readlines()
        # print(lines)

        for line in lines:
            # print(type(line))
            line = line.split()
            # print(line)
            print("line[0]:", line[0])
            image = Image.open(line[0])

            img = image.convert("RGB")

            # img = Image.fromarray((image*255).astype(np.uint8))

            # Image格式转成CV2格式， 然后灰度再转成三通道
            img = cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)  # 变成三通道
            # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 变成单通道
            # img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
            if not os.path.exists(srcimage + "\\label_santongdao"):
                os.mkdir(srcimage + "\\label_santongdao")
            cv2.imwrite(srcimage + "\\label_santongdao\\" + str(index).zfill(4) + ".png", img)  # 把生成图放进指定文件夹
            index += 1


def label_transfer(index):
    with open("label_format.txt") as f:
        lines = f.readlines()
        for line in lines:
            # print(type(line))
            line = line.split()
            print(line[0])
            img = Image.open(line[0])
            img = img.convert("RGB")
            img = cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            for i in range(img.shape[0]):
                for j in range(img.shape[1]):
                    if (img[i, j] != 0):
                        img[i, j] = 255
            if not os.path.exists(srcimage + "\\label_dantongdao"):
                os.mkdir(srcimage + "\\label_dantongdao")
            cv2.imwrite(srcimage+"\\label_dantongdao\\" + str(index).zfill(4) + ".png", img)  # 把生成图放进指定文件夹
            index += 1


if __name__ == '__main__':

    # 用这种方法批量读取图片，顺序不会打乱
    srcimage = r"C:\Users\A3\Desktop\2\\"  # TODO 读取标签图片文件路径
    saveBasePath = "C:\\Users\\A3\\Desktop\\数据预处理\\"  # TODO 保存txt文件路径
    train_id(srcimage, saveBasePath)
    train_txt(srcimage, saveBasePath)

    index = 0 # 图片id起始
    save_img(index) # 保存灰色三通道图像

    # label转成单分类
    label_transfer(index)



