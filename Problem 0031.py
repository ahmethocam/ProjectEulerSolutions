from myTools import *
import math

peni = [1, 2, 5, 10, 20, 50, 100, 200]
indeks = list("01234567")
siralama = []
fak = math.factorial(len(indeks))
print(fak)
for i in range(1,fak):
    indeks = list("01234567")
    siralama.append(permutasyonSirasi(indeks, i))
bulundu=[]
toplananlar=[]

for i in siralama:
    toplam = 0
    for r in i:
        toplam = toplam + peni[int(r)]
        toplananlar.append(peni[int(r)])
        if toplam == 200:
            a = toplananlar.copy()
            bulundu.append(a)
            toplananlar.clear()
            toplam=0
            break
    toplananlar.clear()
print(bulundu)
