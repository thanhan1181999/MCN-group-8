# nhận vào ảnh, chuyển ảnh ra mảng
import numpy as np
import cv2

img = cv2.imread("img1.jpg",0) # https://www.geeksforgeeks.org/python-opencv-cv2-imread-method/
row ,col = img.shape
print(row)
print(col)

# hàm tính toán phần tử trong phần thay đổi, trong các lần phân rã lẻ 1,3,5,7... 
# i là hàng, j là cột, img là mảng 2 chiều pixel
def caculate_change_element_odd(img,i,j):
  row ,col = img.shape
  up = 0
  down =0
  if (i+1) == row: 
    down = 0
    up = img[i-1][j]
  elif i == 0:
    up = 0
    down = img[i+1][j]
  else:
    up = img[i-1][j]
    down = img[i+1][j]
  return int( (up+down)/2 )

# hàm tính toán phần tử trong phần thay đổi, trong các lần phân rã chẵn 2,4,6,8... 
# i là hàng, j là cột, img là mảng 2 chiều pixel
def caculate_change_element_even(img,i,j):
  row ,col = img.shape
  up = 0
  down =0
  if (i+1) == row: 
    down = 0
    up = img[i-1][j]
  elif i == 0:
    up = 0
    down = img[i+1][j]
  else:
    up = img[i-1][j]
    down = img[i+1][j]
  return int( (up+down)/2 )

#------------------------------------------------------------------------------------------------
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
       
        row_h1.append(int( (up+bottom)/2 )
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

#------------------------------------------------------------------------------------------------
row ,col = l1.shape
print(row)
print(col)
list_l2=[] # dải thấp
list_h2=[] # sự thay đổi
for i in range(row):
  row_l2=[] # dải thấp
  row_h2=[] # sự thay đổi
  if (i+1) % 2 == 0: # hàng chẵn thì bỏ đi, cho vào h
    for j in range(col):
      row_h2.append(l1[i,j])
    list_h2.append(row_h2)
  else: # hàng lẻ thì giữ lại cho vào l
    for j in range(col):
      row_l2.append(l1[i,j])
    list_l2.append(row_l2)

h2 = np.array(list_h2)
l2 = np.array(list_l2)
row ,col = l2.shape
print(row)
print(col)
cv2.imwrite("img1-l2.jpg" , l2)

# cv2.imwrite("img1-b1-0.jpg" , img) # https://www.geeksforgeeks.org/python-opencv-cv2-imwrite-method/





