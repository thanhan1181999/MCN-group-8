# nhận vào ảnh, chuyển ảnh ra mảng
import numpy as np
import cv2

img = cv2.imread("img1.jpg",0) # https://www.geeksforgeeks.org/python-opencv-cv2-imread-method/
row ,col = img.shape
# print(img)
# print(type(img)) # numpy.ndarray

# lưu ảnh xám
cv2.imwrite("img1-xam.jpg" , img)

#PROCESS START
list_l1=[] # dải thấp
list_h1=[] # sự thay đổi
for i in range(row): 
  row_l1=[] # dải thấp
  row_h1=[] # sự thay đổi
  if (i+1) % 2 == 0:
    for j in range(col):
      if (j+1) % 2== 1:
        # thêm vào phần h1 
        row_h1.append(img[i,j])
      else:
        # thêm vào l1
        row_l1.append(img[i,j])
  else:
    for j in range(col):
      if (j+1) % 2 == 0:
        row_h1.append(img[i,j])
      else:
        row_l1.append(img[i,j])
  list_l1.append(row_l1)
  list_h1.append(row_h1)

h1 = np.array(list_h1)
l1 = np.array(list_l1)
# cv2.imwrite("img1-h1.jpg" , h1)
cv2.imwrite("img1-l1.jpg" , l1)
# cv2.imwrite("img1-b1-0.jpg" , img) # https://www.geeksforgeeks.org/python-opencv-cv2-imwrite-method/





