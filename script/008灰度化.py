# 灰度化的三种代码
import cv2


# 最大值法
def max_gray(path,img):
    img = img
    grayimg= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            grayimg[i,j] = max(img[i,j][0], img[i,j][1], img[i,j][2])
    cv2.imwrite(path+'max_gray.jpg', grayimg)

#分量法
def sig_gray(path, img):
    img = img
    grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            grayimg[i,j] = img[i,j][0]
    cv2.imwrite(path+'sig_gray.jpg', grayimg)

if __name__=='__main__':
    path = 'C:/Users/17333/Desktop/'
    img = cv2.imread(path+'all.png')
    #img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    #max_gray(path, img)
    #sig_gray(path, img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    cv2.imwrite(path+'all_g.jpg',img)