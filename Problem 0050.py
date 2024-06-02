from myTools import *

asallar = asalSayilar(2, 1000)
seri = []
seri2 = []

for i in asallar:
    seri.append(i)
    for bas in seri:
        seri2.append(bas)
    if TolgaAsalBulma(sum(seri2)):
        print(seri2[0], len(seri2), sum(seri2))
    seri2.clear()

