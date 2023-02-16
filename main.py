

a = [22, 12, 3, 4, 2, 28, 23, 2, 11, 31, 24, 20, 37, 30, 3, 7, 30, 17, 37, 7, 27, 19, 8, 5, 31, 27, 14, 10, 15, 34, 18,
     7, 6, 37, 1, 31, 19, 26, 5, 23, 20, 7, 32, 25, 27, 8, 22, 10, 29, 30, 9, 3, 24, 9, 13, 21, 6, 22, 7, 19, 17, 34,
     16, 14, 32, 32, 16, 20, 24, 33, 4, 8, 8, 12, 9, 16, 14, 30, 3, 36, 17, 20, 11, 24, 18, 10, 28, 37, 30, 17, 7, 22,
     21, 21, 6, 6, 26, 29, 23, 17, 1, 21, 29, 18, 27, 7, 37, 22, 6, 19, 24, 26, 1, 25, 36, 18, 22, 1, 35, 18, 23, 5, 13,
     10, 32, 13, 17, 6, 16, 28, 36, 24, 23, 34, 25, 20, 33, 35, 18, 33, 26, 31, 23, 20, 1, 26, 26, 20, 1, 26, 19, 23]
c = 0
b = 0
for i in a:
    if i < 19 and a != 37:
        c += 1
    else:
        if a != 37:
            b += 1
print('в первой половине', c)
print('во второй половине', b)
l = []
m = []
cc = 0
bb = 0
bol = False
bal = False
oao = False
for i in a:
    if i == 37:
        if bol:
            l += [cc]
            bol = False
        bol = False
    else:
        if bol and i < 19:
            cc += 1
        else:
            if bol:
                l += [cc]
                bol = False
            else:
                if i < 19:
                    bol = True
                    cc = 1


for i in a:

    if bal and i > 18 and i != 37:
        bb += 1
    else:
        if bal:
            m += [bb]
            bal = False
        else:
            if i > 18 and i != 37:
                bal = True
                bb = 1
    if i == 37:
        if bal:
            m += [bb]
            bal = False
        bol = False


print(l)
print(m)
print(sum(l))
print(sum(m))
