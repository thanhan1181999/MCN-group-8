from PIL import Image
import cv2
import numpy
from binary1 import binaryCompress

LINK_IMGAE = 'img1.jpg'
COMPRESSION_TIMES = 1

img = Image.open(LINK_IMGAE) # input ảnh
arr = numpy.array(img) # convert to array from img
row = len(arr) # chiều cao (số hàng)
column = len(arr[0]) # chiều rộng (số cột)

# tách riêng các mảng red green blue
arr_red   = numpy.array([[0 for row in range(column)] for col in range(row)])
arr_green = numpy.array([[0 for row in range(column)] for col in range(row)])
arr_blue  = numpy.array([[0 for row in range(column)] for col in range(row)])
for i in range(row): 
  for j in range(column):
    arr_red[i,j] = arr[i,j][0]
    arr_green[i,j] = arr[i,j][1]
    arr_blue[i,j] = arr[i,j][2]
# khởi tạo
reds = binaryCompress(arr_red,COMPRESSION_TIMES)
greens = binaryCompress(arr_green,COMPRESSION_TIMES)
blues = binaryCompress(arr_blue,COMPRESSION_TIMES)
# encode
reds.encode()
greens.encode()
blues.encode()
# hiện ảnh
result_red = reds.delete_element_0_from_array_image()
result_green = greens.delete_element_0_from_array_image()
result_blue = blues.delete_element_0_from_array_image()
result = numpy.array([[[0,0,0] for row in range(reds.maxlenth)] for col in range(len(result_red))])
for i in range(len(result_red)): 
  for j in range(reds.maxlenth):
    result[i,j][0] = result_red[i,j] 
    result[i,j][1] = result_green[i,j] 
    result[i,j][2] = result_blue[i,j]
cv2.imwrite('image_after_press.jpg',result)
#decode
reds.decode()
greens.decode()
blues.decode()
# hiện ảnh
result_red1 = reds.img
result_green1 = greens.img
result_blue1 = blues.img
result1 = numpy.array([[[0,0,0] for row in range(column)] for col in range(row)])
for i in range(row): 
  for j in range(column):
    result1[i,j][0] = result_red1[i,j] 
    result1[i,j][1] = result_green1[i,j] 
    result1[i,j][2] = result_blue1[i,j]
cv2.imwrite('image_after_decompression.jpg',result1)





