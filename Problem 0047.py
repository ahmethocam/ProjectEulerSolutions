from myTools import *

onceki = 0
seri = 1
for i in range(120000, 150000):
    a = carpanlar(i)
    if len(a) == 4:
        if i - onceki == 1:
            seri = seri + 1
            if seri == 4:
                print(i, onceki,onceki-1,onceki-2)
        else:
            seri = 1
        onceki = i
