# nhận vào ảnh, chuyển ảnh ra mảng
import numpy as np
import cv2

class binaryCompress:
  def __init__(self,img,compression_times):
    # setting binary tree by array
    self.img = cv2.imread(img,0)
    self.compression_times = compression_times
    self.differences = []
    self.row, self.col = self.img.shape

  def initializes_the_array_with_none(self):
    result = []
    for i in range(self.row):
      row_arr = []
      for j in range(self.col):
        row_arr.append(None)
      result.append(row_arr)
    return result

  def convert_to_difference_element(self,time,i,j):
    space = int ( (time+1)/2 )
    up = 0
    down = 0
    if time % 2 == 1: # lần lẻ lấy trên cộng dưới chia 2 - vị trí hiện tại
      if (i-space)<0 :
        up = 0
        down = self.img[i+space,j]
      elif (i+space)>=self.row:
        up = self.img[i-space,j]
        down = 0
      else:
        up = self.img[i-space,j]
        down = self.img[i+space,j]
      return int( (up+down)/2 - self.img[i,j])
    else: # lần chẵn lấy phải trên cộng trái dưới chia 2 - vị trí hiện tại
      if (i+space)>=self.row and (j+space)>=self.col:
        up = 0
        down = 0
      elif (i+space)>=self.row:
        up = self.img[i-space,j+space]
        down = 0
      elif (j+space)>=self.col:
        down = self.img[i+space,j-space]
        up = 0
      else:
        up = self.img[i-space,j+space]
        down = self.img[i+space,j-space]
      return int( (up+down)/2 - self.img[i,j])

  def action_in_odd_time(self,time):
    difference = self.initializes_the_array_with_none()
    for i in range(self.row): 
      if (i+1) % 2 == 0:# hàng chẵn bỏ pixel lẻ
        for j in range(self.col):
          if (j+1) % 2== 1:
            if self.img[i,j]!=0:
              self.img[i,j] = 0
              difference[i][j] = self.convert_to_difference_element(time,i,j)
      else: # hàng lẻ bỏ pixel chẵn
        for j in range(self.col):
          if (j+1) % 2 == 0:
            if self.img[i,j]!=0:
              self.img[i,j] = 0
              difference[i][j] = self.convert_to_difference_element(time,i,j)
    self.differences.append(difference)
  
  def action_in_even_time(self,time):
    difference = self.initializes_the_array_with_none()
    for i in range(self.row): 
      if (i+1) % 2 == 0:# hàng chẵn bỏ 
        for j in range(self.col):
          if self.img[i,j]!=0:
            self.img[i,j] = 0
            difference[i][j] = self.convert_to_difference_element(time,i,j)
    self.differences.append(difference)
    self.delete_element_0_from_array_image()

  def encode(self):
    for time in range(1,self.compression_times+1):
      #nếu lần phân rã lẻ : hàng lẻ bỏ pixel chẵn, hàng chẵn bỏ pixel lẻ
      if time % 2 == 1:
      #nếu lần phân rã chẵn : bỏ hàng chẵn
        self.action_in_odd_time(time)
      else:
        self.action_in_even_time(time)
  
  def delete_element_0_from_array_image(self):
    list = []
    for i in range(self.row):
      arr_row = []
      for j in range(self.col):
        if self.img[i,j]!=0:
          arr_row.append(self.img[i,j]) 
      if arr_row!=[]:
        list.append(arr_row)
    img = np.array(list)
    self.img = img
    self.row,self.col = img.shape

task = binaryCompress("img1.jpg",2)

task.encode()

result = task.img
print(task.img)
print(task.row)
print(task.col)
# print(len(task.differences))
cv2.imwrite("img1-encode-2-time.jpg" , result)
