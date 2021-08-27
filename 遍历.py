import cv2
img = cv2.imread(r"C:\Users\A3\Desktop\2\000060.png")
# img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# index = 0
print(img.shape)
print(img)
# for i in range(img.shape[0]):
#     for j in range(img.shape[1]):
#         # if index < 3000:
#         print(img[i][j])
#         # index += 1


# img = cv2.resize(img,(int(img.shape[1]/3), int(img.shape[0]/3)))
# cv2.imwrite(r"C:\Users\A3\Desktop\2.jpg",img)
