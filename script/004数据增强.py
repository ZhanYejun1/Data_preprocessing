import Augmentor

#图片路径
#p = Augmentor.Pipeline("D:/1veteran/paper/script/image_gray3/")
p = Augmentor.Pipeline(r"C:\Users\A3\Desktop\99")

#图像旋转： 按照概率0.8执行，最大左旋角度5，最大右旋角度5
#p.rotate(probability=0.6, max_left_rotation=5, max_right_rotation=5)

#图像左右互换： 按照概率0.5执行
p.flip_left_right(probability=1)

# 上下互换
p.flip_top_bottom(probability=0.7)

# 对比度变换
p.random_contrast(probability = 0.6,min_factor = 0.6,max_factor = 1.0)

# 随机亮度
p.random_brightness(probability = 0.7,min_factor = 0.6,max_factor = 0.9)

#图像放大缩小： 按照概率0.8执行，面积为原始图0.95倍
p.zoom_random(probability=0.5, percentage_area=0.95)


# 透视形变，垂直方向
#p.skew_tilt(probability=0.6,magnitude=1)

#透视形变，斜四角形变
#p.skew_corner(probability=1,magnitude=1)

# 错切变换
#p.shear(probability=1,max_shear_left=15,max_shear_right=15)

# 增强后的图片
p.sample(120)