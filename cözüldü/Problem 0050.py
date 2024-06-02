from myTools import *

asallar = asalSayilar(2, 10000)
seri = []
seri2 = []
asallar2 =[]
for k in range(len(asallar)):
    asallar2 = asallar[k:].copy()
    for i in asallar2:
        seri.append(i)
        for bas in seri:
            seri2.append(bas)
        if TolgaAsalBulma(sum(seri2)):
            print(seri2[0], len(seri2), sum(seri2))
        seri2.clear()
    seri.clear()