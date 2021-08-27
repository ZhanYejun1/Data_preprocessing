import Augmentor
import glob
import os
import random
# from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img


def image_pro():
    #确定原始图像存储路径以及掩码文件存储路径
    p = Augmentor.Pipeline(r"C:\Users\A3\Desktop\1")  # 加载图像文件  分隔符号只能用/
    p.ground_truth(r"C:\Users\A3\Desktop\2")  # 加载标签文件(只能加004增强标签图转换后的图片) 分隔符号只能用/
    
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
    p.sample(2000)

image_pro()
