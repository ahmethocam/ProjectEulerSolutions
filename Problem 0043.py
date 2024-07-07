from myTools import *
import itertools


perms  = itertools.permutations("0123456789")

cozum = []
asals = (2,3,5,7,11,13,17)
for perm in perms:
    ok = True
    for i in range(1,7):
        s = int(str(perm[i])+str(perm[i+1]+perm[i+2]))
        if s % asals[i-1] != 0:
            ok=False
            break

    if ok:
        print(perm)
        cozum.append(int("".join(perm)))
print(cozum)