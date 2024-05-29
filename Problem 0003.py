# 13195'in asal çarpanları 5, 7, 13 ve 29'dur.
# 600851475143 sayısının en büyük asal çarpanı kaçtır?
import datetime
from myTools import *

sayi = 600851475143

start = datetime.datetime.now()

liste = []
for i in range(2,200000000):
    if sayi % i == 0:
        print(i, sayi / i)
        if TolgaAsalBulma(sayi/i):
            liste.append(sayi/i)
print("Sonuç : ", liste)

finish = datetime.datetime.now()
print("Süre :",finish-start)

