
from math import pow
l=1
for i in range(1,100):
    for k in range(1,101):
        s = int(i**k)
        if len(str(s))==k:
            print(l,i,k,s)
            l+=1

#
# Answer:  49
# Completed on Sun, 7 Jul 2024, 21:28