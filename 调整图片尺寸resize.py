import os
import cv2

source_path="C:/Users/A3/Desktop/999"       #源文件路径
target_path="C:/Users/A3/Desktop/img/0038"        #输出目标文件路径
if not os.path.exists(target_path):
    os.makedirs(target_path)

image_list = os.listdir(source_path)  # 获得文件名

for file in image_list:
    print(file)
    image_source = cv2.imread(os.path.join(source_path,file))  # 读取图片
    image = cv2.resize(image_source, (int(image_source.shape[1]/2.5), int(image_source.shape[0]/2.5)))  # 修改尺寸
    cv2.imwrite(os.path.join(target_path, file), image)  # 重命名并且保存


# for filename in os.listdir("C:/Users/A3/Desktop/video/0000"):
#     print(filename)
#     img = cv2.imread(os.path.join('C:/Users/A3/Desktop/video/0000', filename))
#     res=cv2.resize(img,(int(img.shape[1]/3), int(img.shape[0]/3)))
#     cv2.imwrite(os.path.join('C:/Users/A3/Desktop/video/0000/0000', filename), res)
