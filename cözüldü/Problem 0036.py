import math
from myTools import *

t=0
for i in range(1,1000000):
    if int(terstenYaz(i)) == i and bin(i)[2:] == terstenYaz(bin(i)[2:]):
        print (i,bin(i))
        t+=i
print(t)
