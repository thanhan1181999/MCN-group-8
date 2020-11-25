from PIL import Image
import numpy

img = Image.open('img1.jpg') # input ảnh
arr = numpy.array(img) # convert to array from img
row = len(arr) # chiều cao (số hàng)
column = len(arr[0]) # chiều rộng (số cột)

# cho la 000
for i in range(row): 
  if (i+1) % 2 == 0:
    for j in range(column):
      if (j+1) % 2== 1:
        arr[i,j]=[255,255,255]
  else:
    for j in range(column):
      if (j+1) % 2 == 0:
        arr[i,j]=[255,255,255]

# tách riêng các mảng red green blue
# arr_red   = numpy.array([[0 for row in range(column)] for col in range(row)])
# arr_green = numpy.array([[0 for row in range(column)] for col in range(row)])
# arr_blue  = numpy.array([[0 for row in range(column)] for col in range(row)])
# for i in range(row): 
#   for j in range(column):
#     arr_red[i,j] = arr[i,j][0]
#     arr_green[i,j] = arr[i,j][1]
#     arr_blue[i,j] = arr[i,j][2]
# print(arr_red)
# print(arr_green)
# print(arr_blue)

# create a filtered_arr_red : mang arr_red đã được lọc bước 1
# filtered_arr_red = []
# for i in range(row):
#   filtered_arr_red.append([])
#   if (i+1) % 2 == 0:
#     for j in range(column):
#       if (j+1) % 2== 0:
#         filtered_arr_red[i].append(arr_red[i][j])
#   else:
#     for j in range(column):
#       if (j+1) % 2 == 1:
#         filtered_arr_red[i].append(arr_red[i][j])
# # create a filtered_arr_red : mang arr_red đã được lọc bước 1
# filtered_arr_green = []
# for i in range(row):
#   filtered_arr_green.append([])
#   if (i+1) % 2 == 0:
#     for j in range(column):
#       if (j+1) % 2== 0:
#         filtered_arr_green[i].append(arr_green[i][j])
#   else:
#     for j in range(column):
#       if (j+1) % 2 == 1:
#         filtered_arr_green[i].append(arr_green[i][j])
# # create a filtered_arr_red : mang arr_red đã được lọc bước 1
# filtered_arr_blue = []
# for i in range(row):
#   filtered_arr_blue.append([])
#   if (i+1) % 2 == 0:
#     for j in range(column):
#       if (j+1) % 2== 0:
#         filtered_arr_blue[i].append(arr_blue[i][j])
#   else:
#     for j in range(column):
#       if (j+1) % 2 == 1:
#         filtered_arr_blue[i].append(arr_blue[i][j])

# arr_result_row = len(filtered_arr_blue)
# arr_result_column = len(filtered_arr_blue[0])
# print("arr_result_column : %d" % arr_result_column)
# print("arr_result_row : %d" % arr_result_row)

# print("filtered_arr_blue row : %d" % len(filtered_arr_blue))
# print("filtered_arr_blue column : %d" % len(filtered_arr_blue[0]))
# print("filtered_arr_green row : %d" % len(filtered_arr_green))
# print("filtered_arr_green column : %d" % len(filtered_arr_green[0]))
# print("filtered_arr_red row : %d" % len(filtered_arr_red))
# print("filtered_arr_red column : %d" % len(filtered_arr_red[0]))
# print(filtered_arr_red[659][329])

# arr_result = numpy.array([[[0,0,0] for row in range(arr_result_column)] for col in range(arr_result_row)])
# for i in range(arr_result_row): 
#   for j in range(arr_result_column):
#     arr_result[i,j][0] = filtered_arr_red[i][j]
#     arr_result[i,j][1] = filtered_arr_green[i][j]
#     arr_result[i,j][2] = filtered_arr_blue[i][j]
    # arr_result[i,j][2] = numpy.array(filtered_arr_blue)[i,j]

# trung binh 3 ma mau
# for i in range(row): 
#   if (i+1) % 2 == 0:
#     for j in range(column):
#       if (j+1) % 2== 1:
#         tong=0
#         for t in range(len(arr[i,j])):
#           tong = tong + arr[i,j][t]
#         arr[i,j]=[tong/3,tong/3,tong/3]
#   else:
#     for j in range(column):
#       if (j+1) % 2 == 0:
#         tong=0
#         for t in range(len(arr[i,j])):
#           tong = tong + arr[i,j][t]
#         arr[i,j]=[tong/3,tong/3,tong/3]

# for i in range(row):
#   for j in range(column):
#     if arr[i,j]==[0,0,0]:
#       numpy.delete(arr, i, j)
      
# print(arr_result)
# data = numpy.zeros((330,660, 3), dtype=numpy.uint8)
# data[330,660] = arr_result
new_img = Image.fromarray(arr)

new_img.save("img1-new.jpg")