import numpy as np

a = np.array([1,2,3])
b = np.array(['a','b','c'])

c = np.hstack((a,b))
d = np.vstack((a,b))

print(c,d)

e = np.array([[1,2,3],[4,5,6],[7,8,9]])

f = e[1:3,1:3]

print(f)