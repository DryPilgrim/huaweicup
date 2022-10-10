import numpy as np

data=np.array(
    [1, 2, 3, 4, 5, 6, 7, 8,1, 2, 3, 4, 5, 6, 7, 8,1, 2, 3, 4, 5, 6, 7, 8,1, 2, 3, 4, 5, 6, 7, 8]
).reshape(8,4)

# print(data,type(data))
"""
[[1 2 3 4]
 [5 6 7 8]
 [1 2 3 4]
 [5 6 7 8]
 [1 2 3 4]
 [5 6 7 8]
 [1 2 3 4]
 [5 6 7 8]] <class 'numpy.ndarray'>
"""

print(np.where(data[:]==3))
"""
(array([0, 2, 4, 6], dtype=int64), 
 array([2, 2, 2, 2], dtype=int64))
"""