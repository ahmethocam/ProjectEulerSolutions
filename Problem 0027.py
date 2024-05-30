from myTools import *

def formul(n,a=0,b=0):
    return n*n+a*n+b
liste = []
tamliste=[]
for n in range(1000):
    for a in range(-1000,1000):
        for b in range(-1000,1000):
            s = formul(n,a,b)
            if TolgaAsalBulma(s):
                liste.append(f"{n}-{a}-{s}")
            else:
                continue
        if len(liste)>0:
            tamliste.append(liste.copy())
        if len(liste)>40000:
            print(len(liste),n,a,b)
        liste.clear()
for liste in tamliste:
    if(len(liste)>400):
        print(len(liste),liste)