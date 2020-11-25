# nhận vào ảnh, chuyển ảnh ra mảng
import numpy as np
import cv2

class binaryCompress:
  def __init__(self,img,compression_times):
    # setting binary tree by array
    self.img = cv2.imread(img,0)
    self.compression_times = compression_times
    self.differences = []
        # vd khi compression_times = 6, differences chứa 6 phần tử
        #mỗi phần tử là 1 mảng tương ứng sau mỗi lần phân rã
    self.row, self.col = self.img.shape
    self.DELETE = 0

  # khởi tạo dạng ban đầu của những mảng chứa thông tin thay đổi của ảnh sau khi decode
  def initializes_the_array_with_none(self):
    result = []
    for i in range(self.row):
      row_arr = []
      for j in range(self.col):
        row_arr.append(None)
      result.append(row_arr)
    return result

  # hàm để tạo những giá trị lưu trong mảng (mang thông tin thay đổi của ảnh sau khi decode)
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

  # chuyển đổi để nhận biết hàng chẵn lẻ
  def convert_row_and_column(self,i,space):
    return int((i-1)/space)+1
  
  # hàm tính toán space
  def space(self,time):
    return pow(2,int( (time+1)/2 ) - 1)

  # khi ở bước lẻ, thực hiện xóa xen kẽ
  def action_in_odd_time(self,time):
    difference = self.initializes_the_array_with_none()
    space = self.space(time)
    for i in range(0,self.row,space): 
      if self.convert_row_and_column(i+1,space) % 2 == 0:# hàng chẵn bỏ pixel lẻ
        for j in range(0,self.col,space):
          if self.convert_row_and_column(j+1,space) % 2== 1:
            self.img[i,j] = self.DELETE
            difference[i][j] = self.convert_to_difference_element(time,i,j)
      else: # hàng lẻ bỏ pixel chẵn
        for j in range(0,self.col,space):
          if self.convert_row_and_column(j+1,space) % 2 == 0:
            self.img[i,j] = self.DELETE
            difference[i][j] = self.convert_to_difference_element(time,i,j)
    self.differences.append(difference)
  
  # khi ở bước chẵn, xóa hàng chẵn
  def action_in_even_time(self,time):
    difference = self.initializes_the_array_with_none()
    space = self.space(time)
    for i in range(0,self.row,space): 
      if self.convert_row_and_column(i+1,space) % 2 == 0:# hàng chẵn bỏ 
        for j in range(0,self.col,space):
          self.img[i,j] = self.DELETE
          difference[i][j] = self.convert_to_difference_element(time,i,j)
    self.differences.append(difference)

  # hàm xóa những pixel bị xóa(những ô bị xóa đk gán là 0), để cho ra mảng những pixel còn lại
  def delete_element_0_from_array_image(self):
    list = []
    for i in range(self.row):
      arr_row = []
      for j in range(self.col):
        if self.img[i,j]!=self.DELETE:
          arr_row.append(self.img[i,j]) 
      if arr_row!=[]:
        list.append(arr_row)
    # phát sinh trường hợp số pixel mỗi hàng hơn kém nhau 1 đơn vị
    # sử lý, lấy chiều dài hàng lớn nhất, nếu hàng nào chưa đủ, cho thêm 0
    max = 0
    for i in range(len(list)):
      length = len(list[i])
      if max < length:
        max = length
    #------  
    for i in range(len(list)):
      if len(list[i]) < max:
        list[i].append(0)
    #------
    return np.array(list)

  #hàm main chính
  def encode(self):
    for time in range(1,self.compression_times+1):
      #nếu lần phân rã lẻ : hàng lẻ bỏ pixel chẵn, hàng chẵn bỏ pixel lẻ
      if time % 2 == 1:
      #nếu lần phân rã chẵn : bỏ hàng chẵn
        self.action_in_odd_time(time)
      else:
        self.action_in_even_time(time)
  
  # hàm lưu ảnh
  def save_result_image(self):
    cv2.imwrite("img1-encode-{}-time.jpg".format(self.compression_times), 
      self.delete_element_0_from_array_image())

#=============================Chạy test kết quả================================
task1 = binaryCompress("img1.jpg",1)
task1.encode()
task1.save_result_image()

task2 = binaryCompress("img1.jpg",2)
task2.encode()
task2.save_result_image()

task3 = binaryCompress("img1.jpg",3)
task3.encode()
task3.save_result_image()

task4 = binaryCompress("img1.jpg",4)
task4.encode()
task4.save_result_image()

task5 = binaryCompress("img1.jpg",5)
task5.encode()
task5.save_result_image()

task6 = binaryCompress("img1.jpg",6)
task6.encode()
task6.save_result_image()

task7 = binaryCompress("img1.jpg",7)
task7.encode()
task7.save_result_image()

task8 = binaryCompress("img1.jpg",8)
task8.encode()
task8.save_result_image()

task9 = binaryCompress("img1.jpg",9)
task9.encode()
task9.save_result_image()

task10 = binaryCompress("img1.jpg",10)
task10.encode()
task10.save_result_image()

# lệnh print ra màn hình dùng khi check lỗi 
# r = task5.delete_element_0_from_array_image()
# print("row",len(r))
# for i in range(len(r)):
#   print(len(r[i]))
