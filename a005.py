import numpy as np

a = np.ones((3, 4))
b = np.zeros((3, 2))
print(a)
print(b)
c = np.vsplit(a, [1])
print(c)
