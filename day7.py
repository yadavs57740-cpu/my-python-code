#  day 9

import numpy
# import numpy as np
# from numpy import arange
# from numpy import *
n = numpy.arange(11)
print(type(n))
print(n)
print(n[0])


# example
n = numpy.arange(12)
d = n.reshape(3,4) # 3 -> rows or 4 -> cols
print(type(d))
print(d)

#example 2d
n = numpy.arange(12).reshape(4,3)
print(n)


# example 3d
n = numpy.arange(24).reshape(2,3,4) # 3-> rows or 4 -> cols
print(n)


# example split # 2,5,8,11 -> print
n = numpy.arange(12).reshape(4,3)
print(n)
print(n[0:4:,2]) # first row or second cols
print(n[0:4,2:4]) # first row or second cols
print(n[:,-1])

#example split # 4,7 -> print
n = numpy.arange(12).reshape(4,3)
print(n)
print(n[1:3,1:2])


# day 10

# creating array from list
# 1d , 2d

import numpy as np
# list 1d
l = [1,2,3]
print(l)

# array 1d
arr = np.array(l)
print(arr)

# 2d example

import numpy as np
# 2d list
l = [[1,2,3],[4,5,6]]
print(l)
print(l[0]) # [1,2,3] -> 1row
print(l[0][0]) # [1,2,3] -> 1row -> first element -> 1

# question list value 4 -> 100
l[1][0] = 100
print(l[1])

# 2d array
arr = np.array([[1,2,3],[4,5,6]])
print(arr)
print(arr[0]) # [1,2,3] -> 1 row
print(arr[0][0]) # [1,2,3] -> 1row -> first element -> 1

# question array value 4 -> 100
arr[1][0] = 100
print(arr[1])



#list vs numpy array

# list
l = [1,2,3]
lm = l*2
print(lm)

# array
import numpy as np
arr = np.array(l)
arrM = arr*2
print(arrM)


# comparsion
# array running timing less than list
import numpy as np
import time

# list range(10) -> 0 to 9
start = time.time()
l = [i*2 for i in range(1000000)]
print("list output:",time.time() - start) # 0.06

# array
start = time.time()
arr = np.array(1000000)*2
print("array output:",time.time() - start) # 0.0001


# zeros array 1d
import numpy as np
arr =  np.zeros(5)
print(arr)

# zeros array 2d
arr1 = np.zeros((3,4))
print(arr1)


# ones array 1d
import numpy as np
arr = np.ones(5)
print(arr)
# ones array 2d
arr1 = np.ones((3,4))
print(arr1)


import numpy as np
# question zeros -> 2d array -> 10
arr = np.zeros((2,3))+10
print(arr)
# question ones -> 2d array -> 5
arr1 = np.ones((2,3))+5
print(arr1)


# full for 1d
import numpy as np
arr = np.full((3),5)
print(arr)


# full for 2d
import numpy as np
arr1 = np.full((2,3),5)
print(arr1)

# question help of zeros -> 2d -> 6
import numpy as np
arr = np.zeros((3,4))+6
print(arr)

# question help of full -> 2d -> 1
import numpy as np
arr1 = np.full((3,4),1)
print(arr1)

#random for 1d 0 -> 1
import numpy as np
arr = np.random.random(5)
print(arr)

# random for 2d 0-> 1
arr1 = np.random.random((2,3))
print(arr1)


#arange for 1d
import numpy as np
arr = np.arange(5)
print(arr)

#arange for 1d || to convert into 2d -> reshape
arr1 = np.arange(0,10,2) # start,stop,step
print(arr1)
     


# Vector,matrix,tensor
# vector (1d) , matrix (2d) , tensor (3d)

# question array (2,3) -> (3,2)

import numpy as np
# vector 1d list
l = [1,2,3]
print(l)
#vector 1d array
arr = np.array(l)
print(arr)

#matrix 2d list
l = [[1,2,3],[4,5,6]]
print(l)
#matrix 2d array
arr = np.array(l)
print(arr)

#tensor 3d list
l = [[[1,2],[3,4]],[[5,6],[7,8]]]
print(l)
#tensor 3d array
arr = np.array(l)
print(arr)



# Array properties
# shape , dimension | direction , size , dtype

# array
import numpy as np
arr = np.arange(12) # 1d
# arr = np.arange(12).reshape(3,4) # 3 X 4 => 12  # 2d
print("shape: ",arr.shape)
print("shape: ",np.shape(arr))
print("dimension: ",np.ndim(arr))
print("size: ",np.size(arr))
print("datatype: ",arr.dtype)
     


# day 11

# Array Reshaping

# reshape()
# flatten() -> create copy | shallow copy
# ravel() -> return original | deep copy
# transpose -> .T -> reverse

#reshape array
import numpy as np
arr = np.arange(12) # 12 -> 3*4 || 12 -> 4*3
up_arr = np.reshape(arr,(3,4)) # 3 -> row || 4 -> cols
print(up_arr)

# example 2d
arr1 = np.arange(24)
up_arr1 = np.reshape(arr1,(2*12))
print(up_arr1)

# example 3d
arr2 = np.arange(24)
up_arr2 = np.reshape(arr2,(3*2*4))
print(up_arr2)


#flatten -> create copy then works
import numpy as np
# example 2d
arr = np.arange(12).reshape(3,4)
print(arr)
up_arr = arr.flatten()
print(up_arr)
print(arr)

#example 3d
arr1 = np.arange(24).reshape(3,2,4)
print(arr1)
up_arr1 = arr1.flatten()
print(up_arr1)
     
     
#ravel -> works on original array
import numpy as np
# example 2d
arr = np.arange(14).reshape(7,2)
print(arr)
up_arr = arr.ravel()
up_arr[0] = 100
print(up_arr)
print(arr)

#example ravel 3d
arr1 = np.arange(24).reshape(3,2,4)
print(arr1)
up_arr1 = arr1.ravel()
up_arr1[0] = 100
print(up_arr1)
print(arr1)



# transpose -> rows convert into cols || cols convert into rows
import numpy as np
arr = np.arange(12).reshape(3,4)
print(arr)
up_arr = arr.T
print(up_arr)

# example transpose 3d
arr1 = np.arange(24).reshape(3,2,4)
print(arr1)
up_arr1 = arr1.T
print(up_arr1)


# Numpy Array operations
# slicing for 1d,2d,3d

#slicing for 1d
import numpy as np
arr = np.arange(11)
print(arr)
up_arr = arr[:3]
print(up_arr)

#slicing for 2d
import numpy as np
arr1 = np.arange(16).reshape(8,2)
print(arr1)
up_arr1 = arr1[:,-1]
print(up_arr1)

#slicing for 3d -> arange(24) -> 0,23
import numpy as np
arr2 = np.arange(24).reshape(3,4,2)
print(arr2)
# manually access
# print(arr2[0,0,0],arr2[2,3,1])

# slicing -> 0,23
# print(arr2[::2,::3,0:2:])  # -> ?



# Looping with numpy
# while loop , for loop

# while loop
# while loop for 1d
import numpy as np
arr = np.arange(12)
i = 0
while i < len(arr):
  print(arr[i], end=" ")
  i += 1

# while loop for 2d
import numpy as np
arr1 = np.arange(12).reshape(3,4)
i = 0
len_i = len(arr1)
len_j = len(arr1[i])
while i < len_i:
  j = 0
  while j < len_j:
    print(arr1[i][j], end=" ")
    j += 1
  i += 1

# while loop for 3d
# import numpy as np
# arr1 = np.arange(24).reshape(3,4,2)
# i = 0
# len_i = len(arr1)
# len_j = len(arr1[i])
# len_k = len(arr1[j])
# while i < len_i:
#   j = 0
#   while j < len_j:
#     k = 0
#     while k < len_k:
#      print(arr1[i][j][k], end=" ")
#      k +=1
#     j += 1
#   i += 1

# for loop 1d array

# for loop 2d array

# for loop 3d array


# day 12
# Sorting
# sort() for 1d
# sort() for 2d 

# sort

# 1d
import numpy as np
arr = np.array([10,40,30,60,90,7,5])
print(arr)
arr_s = np.sort(arr)
print(arr_s)

# 2d
# axis = 0 -> cols
# axis = 1 -> rows
import numpy as np
arr1 = np.array([[5,60,20],[40,90,4]])
print(arr1)
arr1_s = np.sort(arr1, axis=0)
print(arr1_s) # default sort -> rows


#example of sort for 2d
import numpy as np
arr1 = np.array([[2,6,3],[20,9,60]])
print(arr1)
# arr1_s = np.sort(arr1)
# print(arr1_s) # default sort -> rows


# by default sorting -> ascending | decending
arr1_s = np.sort(arr1)[::-1]
print(arr1_s)


# Filter
# array[Expression]
# array[array>2] || filter with mask

# filter
# 1d
import numpy as np
arr = np.array([10,20,40,6,3,4,2])
print(arr)
arr_f = arr[arr < 40]
print(arr_f)

# example



# Fancy indexing vs np.where()

#Fancy indexing
import numpy as np
arr = np.array([10,20,3,4,90,100])
print(arr)
arr_f = arr[[0,2]] # 0 index value, 2 index value
print(arr_f)

# example
     


#np.where
import numpy as np
# 1d
arr = np.array([10,3,4,80,30,40,9])
print(arr)
arr_w = np.where(arr>40,"True","False") # condition : True : false
print(arr_w)

# example
arr1 = np.array([10,3,4,80,30,40,9])
print(arr1)
arr_w = np.where(arr>40,arr+2,arr-2) # condition : True : false
# if (arr> 40):
#   arr+2
# else:
#   arr-2
print(arr_w)

# example
     

# Adding and Removing Data

# concatenate
# 1d
import numpy as np
arr1 = np.array([10,20,30])
arr2 = np.array([1,2,3])
#concatenate method
arr1_arr2 = np.concatenate((arr1,arr2))
print(arr1_arr2)
# manually
arr1_arr2_new = arr1 + arr2
print(arr1_arr2_new)

# example 2d
#example 2d array concatenate
import numpy as np
arr1 = np.array([[10,20,30], [40,50,60]])
arr2 = np.array([[70,80,90], [100,110,120]])
print(np.concatenate((arr1,arr2)))
print(np.concatenate((arr1,arr2), axis = 0))


# Statistical Functions