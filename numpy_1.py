# Importing numpy
import np as np
import numpy as np

# Creating an array from a list
list1 = [10, 20, 30]
# print(list1)
arr1 = np.array(list1)
# print(arr1)
# Notice the differences in the output?
# print(type(arr1))

# Using arrange to create an array
# The difference between array and arrange is that array takes a list and makes an array
# Arrange take a range of numbers and makes an array.
arr2 = np.arange(10, 20, 1) # (Start, Stop, Step size)
# print(arr2) # output = [10 11 12 13 14 15 16 17 18 19]

# Multidimensional arrays
# Combining two lists or arrays (2d array) - allows for matrix operations
list2 = [40, 50, 60]
# Join two lists
list3 = [list1, list2]
# Create an array from the joined lists
arr3 = np.array(list3)
# print(arr3)
# Shape of new array
# print(arr3.shape) # output = 2,3

# Three-dimensional arrays
arr3dim = np.array([[[1,2,3],[3,4,5]],[[5,6,7],[7,8,9]]])
print(arr3dim)
# Shape explained (2, 4) output means the Array has 2 dimensions and in EACH dimension there are 4 elements
print(arr3dim.shape)

# Using Arrays and Scalars
# ndarrays let us use matrix operations
# Simple Multiplication -
print(arr3dim * 3)
print(list1 * 3)
# Note the difference, in the ndarray the values are multiplies, in the list it multiplies itself

# You can multiply an array by another array using matrix operations
# Creating an array that is the same size as arr1
arr11 = np.array(list2)
print(arr1 * arr11) # output = 400 1000 1800

# Can you multiply arrays of different shapes?
# No, this gives an error print(arr1 * arr2)
# It is possible to multiply arrays of different dimensions as long as the element size is the same
print(arr1 * arr3dim)

# LAB

# Task 1 - One dimensional array with 12 elements
lab_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
arr_lab = np.array(lab_list)
print(type(arr_lab))
print(arr_lab)

# Task 2 - Two dimensional array size (3,4)
# Not possible, size must be the same in both lists
t2list = [10,20,30]
t2list2 = [50,60,70]
t2list3 = [t2list,t2list2]
twod_array = np.array(t2list3)
print(twod_array.size)

# Task 3 - Three dimensional array size (2,5,4)
t3arr = np.array([[[1,2,3],[3,4,5]],[[5,6,7],[7,8,9]]])
print(t3arr.size)

# Accessing values in ndarrays
# Using arr3 (2d example)

# How can we access the 60 element in arr3?
# We can use indexing
print(arr3[1,2]) # output 60
# To get the bootom row of an array:
print(arr3[1])
# How to get a single column of an array. So all values in the 2 index for example:
print(arr3[:,2]) # output 30 60

# Statistical functions and arrays
# There are many statistical functions built into numpy:

# Finding the total of all sum values
print(arr3.sum) # 210
# Finding the sum of values column-wise
print(arr3.sym(0)) # [50, 70, 90]
# Finding the sum of values row-wise
arr3.sum(1) # [60, 150]
# Finding mean
arr3.mean() # 35.0
# Finding Standard Deviation
arr3.std() # 17.07825127659933
# Finding variance
arr3.var() # 291.6666666666667
# Finding minimum value
arr3.min() # 10
# Finding maximum value
arr3.max() # 60

# Iterating through ndarrays
# If dealing with 1d array:
for x in arr1:
    print(x) # 10 20 30

# If dealing with n-d array, iterate through each dimension until the value is found:
for dim in arr3:
    for num in dim:
        print(num) # 10 20 30 40 50 60

# Alternatively we can use nditer, is neater for nested loops:
for x in np.nditer(arr3):
    print(x) # 10 20 30 40 50 60

# Saving and loading in numpy
# To save an array as a file
np.save("new",arr3)
# Loading the file
np.load("new.npy") # [[10, 20, 30], [40, 50, 60]]
# Saving as txt
np.savetxt("new.txt",arr3,delimiter=',')
# Loading a txt
np.loadtxt("new.txt",delimiter=',') # [[10., 20., 30.], [40., 50., 60.]]









