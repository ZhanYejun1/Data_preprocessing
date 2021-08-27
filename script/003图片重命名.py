import os
import random 
random.seed(0)

# os.listdir读取图片顺序可能会乱
def test(path, num):
    file_names = os.listdir(path)
    c = num
    # 随机获取一张图片的格式
    f_first = file_names[0]

    suffix = f_first.split('.')[-1]  # 图片文件的后缀
    for file in file_names:
        os.rename(os.path.join(path, file), os.path.join(path, '{:0>4d}.{}'.format(c, suffix)))
        c += 1


def deal1(path, n):
    train_percent=1
    temp_img = os.listdir(path)
    total_img = []
    for i in temp_img:
        if i.endswith(".jpg"):  # 根据srcimage图片名修改  eg. jpg png and so on.
            total_img.append(i)
    #print(total_img)
    num=len(total_img)  
    list=range(num)  
    tr=int(num*train_percent)  
    train=random.sample(list,tr)  

    #ftrain = open(os.path.join(saveBasePath,'train.txt'), 'w') 
    c = n
    suffix = 'jpg'
    for i in list:
        if i in train:
            #print(total_img[i])  
            os.rename(os.path.join(path, total_img[i]), os.path.join(path, '{:0>5d}.{}'.format(c, suffix)))
        c += 1

    

if __name__ == '__main__':
    # 修改名称和路径
    n = 58
    path = 'C:/Users/17333/Desktop/test_src/output'
    deal1(path, n)