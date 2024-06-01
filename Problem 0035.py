import itertools
from myTools import *
itertools.product()
asallar = asalSayilar(2,1000000)
asals=[2]
for i in asallar:
    perm=list(str(i))
    if "0" in perm or "2" in perm or "4" in perm or "6" in perm or "8" in perm:
        uygun = False
        continue
    else:
        asals.append(i)
uygunlar = []
for asal in asals:
    uygun = True
    perms = list(itertools.permutations(str(asal)))
    # print (perms)
    for perm in perms:

        p = int("".join(perm))
        if not TolgaAsalBulma(p):
            uygun = False
            break
    if uygun:
        uygunlar.append(asal)


print(uygunlar)
print("Sonuç: ",len(uygunlar))
