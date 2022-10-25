# Importing numpy
 Start at the top of the python file by adding your import statement for numpy. If you do not have numpy installed, Pycharm should show a redline if you do not have it. Easiest to install it from Pycharm if this is the case. Simply click the red lighbulb that appears and click 'install numpy'

`import numpy as np`

### Creating an array from a list
```python
list1 = [10, 20, 30]
print(list1)
arr1 = np.array(list1)
print(arr1)
print(type(arr1))
```
Notice the differences in the output?

### Using arrange to create an array
The difference between array and arrange is that array takes a list and makes an array
#### Arrange takes a range of numbers and makes an array.
```python 
arr2 = np.arange(10, 20, 1) # (Start, Stop, Step size)
print(arr2) # output = [10 11 12 13 14 15 16 17 18 19]
```

### Multidimensional arrays
Combining two lists or arrays (2d array) - allows for matrix operations
``` python 
list2 = [40, 50, 60]
# Join two lists
list3 = [list1, list2]
# Create an array from the joined lists
arr3 = np.array(list3)
print(arr3)
# Shape of new array
print(arr3.shape) # output = 2,3
```

### Three-dimensional arrays
```python
arr3dim = np.array([[[1,2,3],[3,4,5]],[[5,6,7],[7,8,9]]])
print(arr3dim)
print(arr3dim.shape)
```
 Shape explained - (2, 4) output means the Array has 2 dimensions and in EACH dimension there are 4 elements


### Using Arrays and Scalars - ndarrays let us use matrix operations
``` python
# Simple Multiplication -
print(arr3dim * 3)
print(list1 * 3)
```
Note the difference, in the ndarray the values are multiplies, in the list it multiplies itself . You can multiply an array by another array using matrix operations

### Creating an array that is the same size as arr1
```python
arr11 = np.array(list2)
print(arr1 * arr11) # output = 400 1000 1800
```
Can you multiply arrays of different shapes?

No, this gives an error `print(arr1 * arr2)`

It is possible to multiply arrays of different dimensions as long as the element size is the same.
```python 
print(arr1 * arr3dim)
```

## Accessing values in ndarrays -using arr3 (2d example)

How can we access the 60 element in arr3?  We can use indexing:
```python
print(arr3[1,2]) # output 60
```

To get the bottom row of an array:
```python
print(arr3[1])
```
How to get a single column of an array. So all values in the 2 index for example:
```python
print(arr3[:,2]) # output 30 60
```

### Statistical functions and arrays
There are many statistical functions built into numpy:

Finding the total of all sum values
```python
print(arr3.sum) # 210 
```
# Finding the sum of values column-wise
```python
print(arr3.sym(0)) # [50, 70, 90]
```
Finding the sum of values row-wise
```python #
arr3.sum(1) # [60, 150]
```
Finding mean
```python 
arr3.mean() # 35.0
```
Finding Standard Deviation
```python
arr3.std() # 17.07825127659933
```
Finding variance
```python
arr3.var() # 291.6666666666667
```
Finding minimum value
```python
arr3.min() # 10
```
Finding maximum value
```python
arr3.max() # 60
```

## Iterating through ndarrays
If dealing with 1d array:
```python
for x in arr1:
    print(x) # 10 20 30
```

If dealing with n-d array, iterate through each dimension until the value is found:
```python
for dim in arr3:
    for num in dim:
        print(num) # 10 20 30 40 50 60
```
Alternatively we can use nditer, is neater for nested loops:
```python
for x in np.nditer(arr3):
    print(x) # 10 20 30 40 50 60
```

## Saving and loading in numpy
To save an array as a file
```python
np.save("new",arr3)
```
Loading the file
```python
np.load("new.npy") # [[10, 20, 30], [40, 50, 60]]
```
Saving as txt
```python
np.savetxt("new.txt",arr3,delimiter=',')
```
Loading a txt
```python
np.loadtxt("new.txt",delimiter=',') # [[10., 20., 30.], [40., 50., 60.]]
```