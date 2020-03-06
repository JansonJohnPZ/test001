import numpy as np


def lazySum(*arg):
    def sum():
        k = 0
        for i in arg:
            k += i
        return k
    return sum


a = np.arange(10)
print(a)
b = lazySum(a)
print(b)
print(b())
print(b)

