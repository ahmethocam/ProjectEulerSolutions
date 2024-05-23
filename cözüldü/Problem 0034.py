import math


toplam=0
for i in range(3,1000000):
    t=0
    for k in str(i):
        t+=math.factorial(int(k))
    if t == i:
        print (t)
        toplam +=t

print ("Sonuç: ",toplam)

