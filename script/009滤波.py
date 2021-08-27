import cv2

def gauss(path,img):
    gauss_img = cv2.GaussianBlur(img, (3, 3), 0)
    cv2.imwrite(path+'gauss.jpg',gauss_img)

def mean(path,img):
    mean_img = cv2.blur(img, (5,5))
    cv2.imwrite(path+'mean.jpg',mean_img)

def mid(path, img):
    mid_img = cv2.medianBlur(img, 7)
    cv2.imwrite(path+'mid.jpg',mid_img)

if __name__=='__main__':
    path = 'C:/Users/17333/Desktop/sx_gray/'
    img = cv2.imread(path+'cv_gray.jpg')
    mean(path,img)
    mid(path,img)
    gauss(path,img)