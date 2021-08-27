#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 只对jpg格式图片重命名
import os

class ImageRename():
    def __init__(self):
        self.path = r'E:\video\0036'

    def rename(self):
        filelist = os.listdir(self.path)
        total_num = len(filelist)
        print("total_num: ",total_num)

        i = 3656
        for item in filelist:
            # if item.endswith('.png' ):
                src = os.path.join(os.path.abspath(self.path), item)
                dst = os.path.join(os.path.abspath(self.path),  format(str(i).zfill(6), '0>3s') + '.jpg')
                os.rename(src, dst)
                print('converting %s to %s ...' % (src, dst))
                i = i + 1
        print('total %d to rename & converted %d jpgs' % (total_num, i))

if __name__ == '__main__':
    newname = ImageRename()
    newname.rename()
