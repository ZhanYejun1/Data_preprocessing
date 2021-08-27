import cv2
import numpy as np
from PIL import Image
from os import getcwd
import os
import matplotlib.pyplot as plt

import random 
random.seed(0)

# import sys
#
# os.chdir(sys.path[0])


# 生成图片id并保存在txt中
def train_id(srcimage, saveBasePath):
    train_percent=1

    temp_img = os.listdir(srcimage)
    total_img = []
    for i in temp_img:
        if i.endswith(".jpg"):  # 根据srcimage图片名修改  eg. jpg png and so on.
            total_img.append(i)

    num=len(total_img)
    list=range(num)
    tr=int(num*train_percent)
    train=random.sample(list,tr)

    ftrain = open(os.path.join(saveBasePath,'train.txt'), 'w')   # 保存txt文件路径

    for i  in list:  
        name=total_img[i][:-4]+'\n'
        if i in train:  
            ftrain.write(name)  

    ftrain.close()  

# 生成图片id+格式
def train_txt(srcimage, saveBasePath):
    sets=[('2021', 'train')]

    for year, image_set in sets:
        image_ids = open(saveBasePath+'train.txt')
        list_file = open('%s_%s.txt'%(year, image_set), 'w')
        for image_id in image_ids:
            image_id = image_id.split()[0]
            image_id = str(image_id)
            list_file.write(srcimage+'%s.jpg'%(image_id))
            list_file.write('\n')
        list_file.close()



def rand(a=0, b=1):
    return np.random.rand()*(b-a) + a

def mosaic(annotation_line, input_shape, random=True, hue=.1, sat=1.5, val=1.5, proc_img=True):
    '''random preprocessing for real-time data augmentation'''
    h, w = input_shape
    # b = np.random.randint(0, 5)
    # b = b / 10
    # print(b)
    min_offset_x = 0.4
    min_offset_y = 0.4
    scale_low = 1-min(min_offset_x,min_offset_y)
    scale_high = scale_low+0.2

    image_datas = [] 
    index = 0

    place_x = [0,0,int(w*min_offset_x),int(w*min_offset_x)]
    place_y = [0,int(h*min_offset_y),int(w*min_offset_y),0]
    print("annotation:", annotation_line)
    for line in annotation_line:
        # 每一行进行分割
        print("line:",line)
        line_content = line.split()
        print("line_content:",line_content)
        # 打开图片
        image = Image.open(line_content[0])
        image = image.convert("RGB") 
        image = image.resize((416,416),2)
        print(image)
        # 图片的大小
        iw, ih = image.size
        #print(iw,ih)
        
        box = np.array([np.array(list(map(int,box.split(',')))) for box in line_content[1:]])
        
        # image.save(str(index)+".jpg")
        # 是否翻转图片
        flip = rand()<.5
        if flip and len(box)>0:
            image = image.transpose(Image.FLIP_LEFT_RIGHT)
            box[:, [0,2]] = iw - box[:, [2,0]]

        # 对输入进来的图片进行缩放
        new_ar = w/h
        scale = rand(scale_low, scale_high)
        if new_ar < 1:
            nh = int(scale*h)
            nw = int(nh*new_ar)
        else:
            nw = int(scale*w)
            nh = int(nw/new_ar)
        image = image.resize((nw,nh), Image.BICUBIC)

               
        # 将图片进行放置，分别对应四张分割图片的位置
        dx = place_x[index]
        dy = place_y[index]
        new_image = Image.new('RGB', (w,h), (128,128,128))
        new_image.paste(image, (dx, dy))
        #print(type(new_image))
        image_data = np.array(new_image)/255

        #Image.fromarray((image_data*255).astype(np.uint8)).save(str(index)+"distort.jpg")
        Image.fromarray((image_data*255).astype(np.uint8))
        
        index = index + 1
        box_data = []
        # 对box进行重新处理
        if len(box)>0:
            np.random.shuffle(box)
            box[:, [0,2]] = box[:, [0,2]]*nw/iw + dx
            box[:, [1,3]] = box[:, [1,3]]*nh/ih + dy
            box[:, 0:2][box[:, 0:2]<0] = 0
            box[:, 2][box[:, 2]>w] = w
            box[:, 3][box[:, 3]>h] = h
            box_w = box[:, 2] - box[:, 0]
            box_h = box[:, 3] - box[:, 1]
            box = box[np.logical_and(box_w>1, box_h>1)]
            box_data = np.zeros((len(box),5))
            box_data[:len(box)] = box
        
        image_datas.append(image_data)
        
           
    # 将图片分割，放在一起
    cutx = np.random.randint(int(w*min_offset_x), int(w*(1 - min_offset_x)))
    cuty = np.random.randint(int(h*min_offset_y), int(h*(1 - min_offset_y)))

    new_image = np.zeros([h,w,3])
    new_image[:cuty, :cutx, :] = image_datas[0][:cuty, :cutx, :]
    new_image[cuty:, :cutx, :] = image_datas[1][cuty:, :cutx, :]
    new_image[cuty:, cutx:, :] = image_datas[2][cuty:, cutx:, :]
    new_image[:cuty, cutx:, :] = image_datas[3][:cuty, cutx:, :]

    return new_image


def save_mosaic_img(index):
    with open("2021_train.txt") as f:
        lines = f.readlines()

    a = np.random.randint(0, len(lines))
    np.random.shuffle(lines)
    line = lines[a : a+4]
    img = mosaic(line, [416, 416])
    
    img = Image.fromarray((img*255).astype(np.uint8))
    # img = cv2.cvtColor(np.asarray(img),cv2.COLOR_RGB2BGR) 
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    #cv2.imwrite("C:/Users/17333/Desktop/test_src/" + str(index).zfill(5)+".jpg", img)
    img.save(srcimage + str(index).zfill(5)+".jpg")  # TODO 这里改一下保存mosaic变换后的图片路径
    
    #img.show()

def save_img(index):
    with open("2021_train.txt") as f:
        lines = f.readlines()
        #print(lines)
        
        for line in lines:
            #print(type(line))
            line = line.split()
            print(line[0])
            image = Image.open(line[0])

            img = image.convert("RGB") 
            
            #img = Image.fromarray((image*255).astype(np.uint8))

            # Image格式转成CV2格式， 然后灰度再转成三通道
            img = cv2.cvtColor(np.asarray(img),cv2.COLOR_RGB2BGR) 
            # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
            
            cv2.imwrite("C:/Users/17333/Desktop/new_png/" + str(index).zfill(4)+".png", img)
            index += 1

def label_transfer(index):
    with open("2021_train.txt") as f:
        lines = f.readlines()
        for line in lines:
            #print(type(line))
            line = line.split()
            print(line[0])
            img = Image.open(line[0])
            img = img.convert("RGB")
            img = cv2.cvtColor(np.asarray(img),cv2.COLOR_RGB2BGR) 
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            for i in range(img.shape[0]):
                for j in range(img.shape[1]):
                    if(img[i,j] != 0):
                        img[i,j] = 255
            cv2.imwrite("C:/Users/A3/Desktop/video/0012/" + str(index).zfill(4)+".png", img)
            index += 1


if __name__ == '__main__':

    #用这种方法批量读取图片，顺序不会打乱
    srcimage = "C:\\Users\\A3\\Desktop\\video\\0002\\"  # TODO 读取图片文件路径
    saveBasePath = "C:\\Users\\A3\\Desktop\\script\\"  # TODO 保存txt文件路径
    train_id(srcimage, saveBasePath)
    train_txt(srcimage, saveBasePath)

    # index = 0 # 图片id起始
    # save_img(index) # 保存灰色三通道图像

    num = 4  # TODO mosaic生成的图片数量，小于等于总图片数量/4
    index_mosaic = 18  #TODO  mosaic生成图片起始id  eg 0000.jpg 大于原图片索引
    # 保存mosaic图像
    while(num):
        save_mosaic_img(index_mosaic)
        num -= 1
        index_mosaic += 1
    
    #label转成单分类
    #label_transfer(index)
    #plt.imshow()



