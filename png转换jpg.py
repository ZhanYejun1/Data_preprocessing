#!/usr/bin/env python
# OpenCV把当前文件夹下的png批量转为jpg
from glob import glob
import cv2
pngs = glob(r'C:\Users\A3\Desktop\powerline\*.png')

for j in pngs:
    img = cv2.imread(j)
    cv2.imwrite(j[:-3] + '.jpg', img)
