from myTools import *
onceki = 0
for i in range(50000,100000):
    a  = carpanlar(i)
    if len(a)==4:
        if i-onceki == 1:
            print(i,onceki)
        onceki = i

