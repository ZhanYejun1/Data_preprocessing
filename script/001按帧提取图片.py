import cv2
import time
import os

input_video = 'D:/Python/4test/6.avi'
output_dir = 'D:/Python/A_image/test/'
 
if not os.path.exists(output_dir):  #判断是否存在文件夹如果不存在则创建为文件夹
    os.makedirs(output_dir)


START_TIME= 0 #设置开始时间(单位秒)
END_TIME= 2000 #设置结束时间(单位秒)
 
vidcap = cv2.VideoCapture(input_video)
 
fps = int(vidcap.get(cv2.CAP_PROP_FPS))     # 获取视频每秒的帧数
print("fps: ", fps)
 
frameToStart = START_TIME*fps               #开始帧 = 开始时间*帧率
print("frameToStart: ", frameToStart)
frametoStop = END_TIME*fps                  #结束帧 = 结束时间*帧率
print("frameToStop: ", frametoStop)
 
vidcap.set(cv2.CAP_PROP_POS_FRAMES, frameToStart) #设置读取的位置,从第几帧开始读取视频
print(vidcap.get(cv2.CAP_PROP_POS_FRAMES))  # 查看当前的帧数
 
success,frame = vidcap.read()               # 获取第一帧
 
count = 0
seconds = 2
i = 0
while success and frametoStop >= count:
    if count % (fps*seconds) == 0:          # 每second秒保存一次
        #save_path = output_dir + str(count) + ".jpg"
        #print(count)
        fileName = str(104+i) + '.jpg'        # 修改数字改名字
        cv2.imwrite(os.path.join(output_dir, fileName),frame,[cv2.IMWRITE_JPEG_QUALITY,100])       # 保存图片
        print('Process %dth seconds: ' % int(count / (fps*seconds)), success)
        i += 1
    success,frame = vidcap.read()           # 每次读取一帧
    count += 1
 
print("end!")
 





