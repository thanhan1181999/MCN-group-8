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
  def convert_to_difference_element(self,time,i,j): # 7 2
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
      return int((up+down)/2) - self.img[i,j]
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
      return int((up+down)/2) - self.img[i,j]

   # hàm để tạo những giá trị lưu trong mảng (mang thông tin thay đổi của ảnh sau khi decode)

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
            difference[i][j] = self.convert_to_difference_element(time,i,j)
            self.img[i,j] = self.DELETE
      else: # hàng lẻ bỏ pixel chẵn
        for j in range(0,self.col,space):
          if self.convert_row_and_column(j+1,space) % 2 == 0:
            difference[i][j] = self.convert_to_difference_element(time,i,j)
            self.img[i,j] = self.DELETE
    self.differences.append(difference)
  
  # khi ở bước chẵn, xóa hàng chẵn
  def action_in_even_time(self,time):
    difference = self.initializes_the_array_with_none()
    space = self.space(time)
    for i in range(0,self.row,space): 
      if self.convert_row_and_column(i+1,space) % 2 == 0:# hàng chẵn bỏ 
        for j in range(space,self.col,space*2):
          difference[i][j] = self.convert_to_difference_element(time,i,j)
          self.img[i,j] = self.DELETE
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
    print("max length : ",max)
    for i in range(len(list)):
      while len(list[i]) < max:
        list[i].append(0)
    #------
    return np.array(list)

  #hàm nén ảnh
  def encode(self):
    for time in range(1,self.compression_times+1):
      #nếu lần phân rã lẻ : hàng lẻ bỏ pixel chẵn, hàng chẵn bỏ pixel lẻ
      if time % 2 == 1:
      #nếu lần phân rã chẵn : bỏ hàng chẵn
        self.action_in_odd_time(time)
      else:
        self.action_in_even_time(time)
  #----------------------------------------------------------------------------------------------------

  # hàm trả về giá trị pixel cỉa ảnh gốc
  def convert_difference_element_back(self,time,i,j,difference):
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
      return int( (up+down)/2 - difference[i][j])
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
      return int( (up+down)/2 - difference[i][j])

  # hàm lưu ảnh
  def save_result_image(self,type = 0):
    if type != 0:
      file_name = "img-decode-{}-time.jpg".format(self.compression_times) 
    else:
      file_name = "img-encode-{}-time.jpg".format(self.compression_times) 
    cv2.imwrite(file_name, self.delete_element_0_from_array_image())

  # hàm giải mã ảnh về ban đầu
  def decode(self):
    for i in range(self.compression_times-1,-1,-1):
      space = self.space(i+1)
      for x in range(0,self.row,space):
        for y in range(0,self.col,space):
          if self.differences[i][x][y] is not None:
            self.img[x,y] = self.convert_difference_element_back(i+1,x,y,self.differences[i])
              
  # lưu các mảng chứa phần thay đổi ra file
  # def save_diffence_to_file(self):
  #   for i in range(len(self.differences)):
  #     file = open("diff-{}.txt".format(i+1), "w")
  #     difference = self.differences[i]
  #     for x in range(self.row):
  #       for y in range(self.col):
  #         file.write(  "{} ".format(difference[x][y]) )
  #     file.close()

  #----------------------------------------------------------------------------------------------------
  # def print_diff(self,i):
  #   for i in range(self.compression_times-1,-1,-1):
  #   print(self.differences[i])
  # def print_img(self):
  #   print(self.img)
        
#=============================Chạy test kết quả================================
# task1 = binaryCompress("img_test.jpg",2)
# print(task1.convert_to_difference_element(1,7,2))
# task1.encode()
# task1.print_img()
# task1.print_diff(1)
# task1.print_diff()
# print(task1.convert_to_difference_element(1,0,3))
# task1.save_result_image()
# task1.save_diffence_to_file()
# task1.decode()
# task1.print_img()
# task1.save_result_image()

task1 = binaryCompress("img1.jpg",5)
task1.encode()
task1.save_result_image()
task1.decode()
task1.save_result_image(1)


# task2 = binaryCompress("img3.jpg",2)
# task2.encode()
# task2.save_result_image()

# task3 = binaryCompress("img3.jpg",3)
# task3.encode()
# task3.save_result_image()

# task4 = binaryCompress("img3.jpg",4)
# task4.encode()
# task4.save_result_image()

# task5 = binaryCompress("img3.jpg",5)
# task5.encode()
# task5.save_result_image()

# task6 = binaryCompress("img3.jpg",6)
# task6.encode()
# task6.save_result_image()

# task7 = binaryCompress("img1.jpg",7)
# task7.encode()
# task7.save_result_image()

# task8 = binaryCompress("img1.jpg",8)
# task8.encode()
# task8.save_result_image()

# task9 = binaryCompress("img1.jpg",9)
# task9.encode()
# task9.save_result_image()

# task10 = binaryCompress("img1.jpg",10)
# task10.encode()
# task10.save_result_image()

# lệnh print ra màn hình dùng khi check lỗi 
# r = task5.delete_element_0_from_array_image()
# print("row",len(r))
# for i in range(len(r)):
#   print(len(r[i]))

# print(len(task4.differences))
# print(task4.differences[0])
# https://www.kite.com/python/answers/how-to-save-a-numpy-array-to-a-text-file-in-python#:~:text=Use%20numpy.,array%20to%20a%20text%20file&text=Use%20a%20for%2Dloop%20to,to%20the%20opened%20file%20fname%20.&text=The%20resulting%20text%20file%20can%20be%20loaded%20back%20into%20an%20array%20.
# for i in range(len(task4.differences)):
#   dif = np.array(task4.differences[i])
#   file_name = "diff_{}.txt".format(i)
#   a_file = open(file_name, "w")
#   for row in dif:
#     np.savetxt(file_name, row)
#   a_file.close()
