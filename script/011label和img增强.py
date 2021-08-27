import Augmentor
import glob
import os
import random
# from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img

train_path = r'‪C:\Users\A3\Desktop\99'
groud_truth_path = r'‪C:\Users\A3\Desktop\55'
train_type = 'jpg'
mask_type = 'png'
train_tmp_path = r'‪C:\Users\A3\Desktop\88'
mask_tmp_path = r'‪C:\Users\A3\Desktop\44'

def start(train_path,groud_truth_path):
    train_img = glob.glob(train_path+'/*.'+train_type)
    masks = glob.glob(groud_truth_path+'/*.'+mask_type)
 
    if len(train_img) != len(masks):
        print ("trains can't match masks")
        return 0
    for i in range(len(train_img)):
        train_img_tmp_path = train_tmp_path
        if not os.path.lexists(train_img_tmp_path):
            os.mkdir(train_img_tmp_path)
        img = load_img(train_path+'/'+str(i).zfill(4)+'.'+train_type)
        x_t = img_to_array(img)
        img_tmp = array_to_img(x_t)
        img_tmp.save(train_img_tmp_path+'/'+str(i).zfill(4)+'.'+train_type)
 
        mask_img_tmp_path =mask_tmp_path
        if not os.path.lexists(mask_img_tmp_path):
            os.mkdir(mask_img_tmp_path)
        mask = load_img(groud_truth_path+'/'+str(i).zfill(4)+'.'+mask_type)
        x_l = img_to_array(mask)
        mask_tmp = array_to_img(x_l)
        mask_tmp.save(mask_img_tmp_path+'/'+str(i).zfill(4)+'.'+mask_type)
        print ("%s folder has been created!"%str(i).zfill(4))
    return i + 1

def doAugment(num):
    sum = 0
    for i in range(num):
        p = Augmentor.Pipeline(train_tmp_path+'/'+str(i).zfill(4))
        p.ground_truth(mask_tmp_path+'/'+str(i).zfill(4))
        p.rotate(probability=0.5, max_left_rotation=5, max_right_rotation=5)#旋转
        p.flip_left_right(probability=0.5)#按概率左右翻转
        #p.zoom_random(probability=0.6, percentage_area=0.99)#随即将一定比例面积的图形放大至全图
        p.flip_top_bottom(probability=0.6)#按概率随即上下翻转
        #p.random_distortion(probability=0.8,grid_width=10,grid_height=10, magnitude=20)#小块变形
        #图像左右互换： 按照概率0.5执行
        p.flip_left_right(probability=0.6)
        # 随机亮度
        p.random_brightness(probability = 0.6,min_factor = 0.6,max_factor = 1.0)
        count = random.randint(10000,12000)
        print("\nNo.%s data is being augmented and %s data will be created"%(i,count))
        sum = sum + count
        p.sample(count)
        print("Done")
    print("%s pairs of data has been created totally"%sum)

def image_pro():
    #确定原始图像存储路径以及掩码文件存储路径
    p = Augmentor.Pipeline("C:/Users/A3/Desktop/1")  # 加载图像文件
    p.ground_truth("C:/Users/A3/Desktop/2/label_santongdao")  # 加载标签文件
    
    #图像旋转： 按照概率0.8执行，最大左旋角度10，最大右旋角度10
    p.rotate(probability=0.8, max_left_rotation=10, max_right_rotation=10)
    
    #图像左右互换： 按照概率0.5执行
    p.flip_left_right(probability=0.5)
    
    #图像放大缩小： 按照概率0.8执行，面积为原始图0.85倍
    p.zoom_random(probability=0.3, percentage_area=0.85)

    p.skew_corner(probability=0.3,magnitude=1)
    
    p.shear(probability=0.4,max_shear_left=15,max_shear_right=15)

    p.random_brightness(probability = 0.2,min_factor = 0.4,max_factor = 0.7)

    #最终扩充的数据样本数
    p.sample(4000)

# a = start(train_path, groud_truth_path)
# doAugment(a)
image_pro()
