# 13195'in asal çarpanları 5, 7, 13 ve 29'dur.
# 600851475143 sayısının en büyük asal çarpanı kaçtır?

import math

sayi = 600851475143
carpanlar = []
asallar = []
for i in range(sayi//30,sayi // 2,2):
    if sayi % i == 0:
        print(i)
        carpanlar.append(i)
print(list(carpanlar))


for i in carpanlar:
    asaldegil = False
    for k in range(2, i):
        if i % k == 0:
            asaldegil = True
            break
    if asaldegil == False:
        print(i)
        asallar.append(i)

print(list(asallar.sort()))
