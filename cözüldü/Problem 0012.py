import datetime
from myTools import *
import math
start = datetime.datetime.now()

print(math.factorial(10))
print(math.factorial(11))
kk=[]
ts=[]

for i in range(11660,11661):
    ts.append(int(i * (i + 1) / 2))

for s in ts:
    for k in range(1, int(s / 2) + 1):
        if s % k == 0:
            kk.append(k)
    if len(kk) > 100:
        print(s,len(kk))
    kk.clear()
finish = datetime.datetime.now()
print("Süre :",finish-start)


#cevap: 76576500 575