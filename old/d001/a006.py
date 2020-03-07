import numpy as np

def mm(*num):
    t = 0
    for i in num:
        t += i
    return t


a = 1
b = 2
c = 3
d = 4
e = np.arange(1, 9, 1)
print(e)

t = mm(*e)

print(t)