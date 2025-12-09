import numpy as np
tableau_1d = np.array([1, 2, 3, 4, 5])
tableau_2d = np.array([[1, 2, 3],
                       [4, 5, 6]])

zeros = np.zeros((2, 3))
ones = np.ones((3, 2))
progression = np.arange(0, 10, 2)
linspace = np.linspace(0, 1, 5)
def info(arr, name):
    print(f" {name}")
    print(arr)
    print("dtype :", arr.dtype) 
    print("ndim  :", arr.ndim) 
    print("shape :", arr.shape) 
    print("size  :", arr.size)   
    print()
info(tableau_1d, "tableau_1d")
info(tableau_2d, "tableau_2d")
info(zeros, "zeros")
info(ones, "ones")
info(progression, "progression")
info(linspace, "linspace")
