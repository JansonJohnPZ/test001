import numpy as np


def showAll(p):
    print('*'*16)
    print(p)
    print('dim: ', p.ndim)
    print('shape: ', p.shape)
    print('dtype: ', p.dtype)


a = np.array([
    [1, 2, 3],
    [4, 5, 6]
], dtype=np.int64)
showAll(a)

b = np.ones((3, 1), dtype=np.int64)
showAll(b)

c = np.zeros((5, 4), dtype=np.int64)
showAll(c)

d = np.empty((2, 2), dtype=np.int64)
showAll(d)

e = np.arange(0, 100, 20)
showAll(e)

f = np.linspace(0, 100, 20)
showAll(f)

g = np.linspace(-19, 812, 7*6).reshape(7, 6)
showAll(g)
