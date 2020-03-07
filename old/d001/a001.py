def findAll(str, cha):
    tip = 0
    en = []
    while(True):
        temp = str.find(cha, tip)
        if temp == -1:
            tip += 1
            temp = str.find(cha, tip)
            if temp == -1:
                break
        else:
            en.append(temp)
            tip = temp + 1
    return en

str = 'abcd' * 12
print(str)
en = findAll(str, 'a')
print(en)

for i in en:
    print(str[i])
