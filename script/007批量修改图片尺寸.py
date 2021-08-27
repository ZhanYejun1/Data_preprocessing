import cv2
import os
 
                #设定尺寸
source_path=r"C:\Users\A3\Desktop\video\0013/"       #源文件路径
target_path=r"C:\Users\A3\Desktop\12/"        #输出目标文件路径
 
if not os.path.exists(target_path):
    os.makedirs(target_path)
 
image_list = os.listdir(source_path)      #获得文件名
 
i=0
for file in image_list:
    image_source=cv2.imread(source_path+file)  # 读取图片
    image = cv2.resize(image_source, (416, 416),0,0, cv2.INTER_LINEAR)#修改尺寸
    cv2.imwrite(target_path+str(i).zfill(4)+".jpg",image)           #重命名并且保存
    i=i+1
print("批量处理完成")