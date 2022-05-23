import numpy as np
from io import BytesIO

# Numpy ndarray
arr = np.array([1, 3, 4, 5, 6])
arr

arr.shape
arr.dtype

arr = np.array([1, 'st', 'er', 3])
arr.dtype

# Creating Arrays
arr = np.array([[1, 2, 3], [2, 4, 6], [8, 8, 8]])
arr.shape
arr

# np.zeros: Creates a matrix of specified dimensions containing only zeroes
arr = np.zeros((2, 4))
arr

# np.ones: Creates a matrix of specified dimension containing only ones
arr = np.ones((2, 4))
arr

# np.identity: Creates an identity matrix of specified dimensions
arr = np.identity(3)
arr

# Initialize an array of a specified dimension with random values
arr = np.random.randn(3, 4)
arr

# Read data from text file to a numpy array
b = BytesIO(b"2,23,33\n32,42,63.4\n35,77,12")
arr = np.genfromtxt(b, delimiter=",")
arr

# Accessing Array Elements
arr[1]

arr = np.arange(12).reshape(2, 2, 3)
arr

arr[0]

arr = np.arange(10)
arr[5:]
arr[5:8]
arr[:-5]

arr = np.arange(12).reshape(2, 2, 3)
arr
arr[1:2]

arr = np.arange(27).reshape(3, 3, 3)
arr
arr[:, :, 2]  # Access the third column

arr[..., 2]  # Access the third column using e a dot notation

arr = np.arange(9).reshape(3, 3)
arr
arr[[0, 1, 2], [1, 0, 0]]

# Boolean indexing
cities = np.array(["delhi", "bangalore", "mumbai", "chennai", "bhopal"])
cities
city_data = np.random.randn(5, 3)
city_data

city_data[cities == "delhi"]
city_data[city_data > 0]

city_data[city_data > 0] = 0
city_data

# Operations on Arrays
arr = np.arange(15).reshape(3, 5)
arr
arr + 5
arr * 2

arr1 = np.arange(15).reshape(5, 3)
arr2 = np.arange(5).reshape(5, 1)
arr2 + arr1

arr1
arr2

arr1 = np.random.randn(5, 3)
arr1
np.modf(arr1)

# Linear Algebra Using numpy
A = np.array([[1,2,3],[4,5,6],[7,8,9]])
B = np.array([[9,8,7],[6,5,4],[1,2,3]])

A.dot(B)

A = np.arange(15).reshape(3,5)
A.T

np.linalg.svd(A)

a = np.array([[7,5,-3], [3,-5,2],[5,3,-7]])
b = np.array([16,-8,0])
x = np.linalg.solve(a, b)
x

np.allclose(np.dot(a, x), b)