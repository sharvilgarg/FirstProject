import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])

print(a)

print('Indices of elements <4')

b = np.where(a < 4)
print(b)

print("Elements which are <4")
print(a[b])