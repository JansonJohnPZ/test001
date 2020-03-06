#D:\trr.txt

str = r'D:\wqeqweqe\qweqweqwe\qweqweq\trr.txt'
print(str)
k = str.rfind('\\')
if k == -1:
    print('err01')
else:
    print(str[k+1:])