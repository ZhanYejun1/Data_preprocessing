'''
先把log文件名存储在txt文件中，检查是否乱序，然后逐行读取txt中的loss值和epoch数，进行loss绘制
'''

import os,sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import re
                                                                                       
# logs文件名存储在txt文件中
def ListFilesToTxt(dir, file, wildcard, recursion):
    exts = wildcard.split(" ")
    print(exts)
    files = os.listdir(dir)
    for name in files:
        fullname = os.path.join(dir, name)
        if (os.path.isdir(fullname) & recursion):
            ListFilesToTxt(fullname, file, wildcard, recursion)
        else:
            for ext in exts:
                if (name.endswith(ext)):
                    file.write(name + "\n")
                    break

def ReadName():
    dir = r"C:\Users\A3\Desktop\loss绘制"  # 读取文件路径
    outfile = "C:/Users/A3/Desktop/loss1.txt"  # 将文件名写入loss.txt
    wildcard = ".pth"
    #   wildcard = ".jpg .txt .exe .dll .lib"等等      #要读取的文件类型
    file = open(outfile, "w")
    if not file:
        print("cannot open the file %s for writing" % outfile)
    ListFilesToTxt(dir, file, wildcard, 1)
    file.close()

#先转化成text文件(注意：可能会乱序）， 然后手动删除epoch，最后调用loss进行绘制
def loss(path):
    t_loss=[]
    v_loss=[]
    epoch = []

    # 对txt文件每一行读取
    fopen=open(path,'r')
    lines=fopen.readlines()
    
    i=1
    for line in lines:
        line = line.strip('\n') #去掉换行符
        line = line.replace('Epoch', '', 1).replace(str(i)+'-Total_Loss', '', 1).replace('-Val_Loss', ',', 1).replace('.pth', '', 1)
        #print(line)
        t_loss.append(line.split(',')[0].split(' ')[-1])
        v_loss.append(line.split(',')[-1])
        epoch.append(i)
        i += 1
        #print(type(line))

    del t_loss[-1], v_loss[-1], epoch[-1]
    t_loss = [float(x) for x in t_loss]
    v_loss = [float(x) for x in v_loss]
    # print(t_loss)
    # print(v_loss)
    # print(epoch)t

    # 绘制loss曲线图
    zhfont1 = matplotlib.font_manager.FontProperties(fname="C:/Users/17333/Desktop/SourceHanSansSC-Bold.otf") 
    plt.plot(epoch, t_loss)
    plt.title("Loss曲线", fontproperties=zhfont1, fontsize = 15) 
    plt.xlabel("训练世代") 
    plt.ylabel("损失值")
    plt.savefig('C:/Users/17333/Desktop/t_loss.jpg')   
    plt.show()

def loss_hand(path):
    t_loss=[]
    epoch = [1]

    # 对txt文件每一行读取
    fopen=open(path,'r')
    lines=fopen.readlines()
    
    for line in lines:
        line = line.strip('\n')
        print(line)
        t_loss.append(line)
    print(t_loss)
    print(len(t_loss))

    #del t_loss[-1], v_loss[-1], epoch[-1]
    t_loss = [float(x) for x in t_loss]
    print(t_loss)
    # print(v_loss)
    # print(epoch)t

    for i in range(500):
        if (i % 10 == 0) and i!=0:
            epoch.append(i)
    print(epoch)
    print(len(epoch))

    #绘制loss曲线图
    zhfont1 = matplotlib.font_manager.FontProperties(fname=r"‪C:\Users\A3\Desktop\loss绘制\SourceHanSansSC-Bold.otf")
    plt.plot(epoch, t_loss)
    plt.title("Loss曲线", fontproperties=zhfont1, fontsize = 15) 
    plt.xlabel("训练世代", fontproperties=zhfont1, fontsize = 15) 
    plt.ylabel("损失值", fontproperties=zhfont1, fontsize = 15)
    plt.savefig('C:/Users/A3/Desktop/t_loss1.jpg')
    plt.show()

if __name__ == '__main__':
    ReadName()
    path = 'C:/Users/A3/Desktop/loss1.txt'
    loss_hand(path)


