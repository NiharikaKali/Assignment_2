###1. Numpy
###Using NumPy create random vector of size 15 having only Integers in the range 1-20.
###1. Reshape the array to 3 by 5
###2. Print array shape.
###3. Replace the max in each row by 0
import numpy as np
np.__version__

arr = np.random.randint(1, 21, 15)
arr
print(arr)
#1
arr2 = arr.reshape((3,5))
arr2

#2
print(arr2.shape)

#3
np.where(arr2 == arr2.max(axis = 1)[:,None], 0, arr2)
print(arr2)
