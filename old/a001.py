import numpy as np


def decorate(func):
    def funcIn(*args, **kwargs):
        print('nmsl1')
        func(*args, **kwargs)
        print('nmsl2')
    return funcIn


@decorate
def yu(a, b):
    print(a+b)


a = 3
b = 4
yu(a, b)
