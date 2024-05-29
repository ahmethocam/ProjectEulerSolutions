import math

belirlenmisAsalSayilar = []
""" 2.000.000 a kadar hesaplanan asal sayılar"""


def rakamlarToplami(sayi):
    f = 0
    for j in str(sayi):
        f += int(j)
    return f


def birlerBasamagi(sayi):
    return int(str(sayi)[-1])


def sonBasamaklar(sayi, adet):
    if len(str(sayi)) <= adet:
        return sayi
    return int(str(sayi)[-1 * adet:])


def ilkBasamaklar(sayi, adet):
    if len(str(sayi)) <= adet:
        return sayi
    return int(str(sayi)[:adet])


def terstenYaz(yazi):
    txt = str(yazi)[::-1]
    return txt


def asalSayilar(min=2, max=1000):
    asallar = []
    for i in range(min, max):
        if i % 1000 == 0:
            print(i)
        if asalmi(i):
            asallar.append(i)
    return asallar


def asalmi(sayi):
    s = math.floor(math.sqrt(sayi))
    a = asalSayilar(2, s + 1)
    asal = True
    for k in a:
        if sayi % k == 0:
            asal = False
            break
    return asal


def EasalSayilar(min=2, max=1000):
    asallar = [2]
    for i in range(3, max):
        if i % 1000 == 0:
            print(i)
        if Easalmi(i):
            asallar.append(i)
    return asallar


def Easalmi(sayi):
    asal = True
    if str(sayi)[-1] == "5":
        return False
    for k in range(2, int(sayi / 2), 2):
        if sayi % k == 0:
            asal = False
            break
    return asal


# 1709600813

def AsalOlmayanlar(max):
    olabilecek = []
    for i in range(max):
        if i % 2 != 0 and str(i)[-1] != "5" and rakamlarToplami(i) % 3 != 0:
            olabilecek.append(i)
    return olabilecek


def TolgaAsalBulma(sayi):
    if sayi % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(sayi)) + 1, 2):
        if sayi % i == 0:
            return False
    return True


def yerDegistir(st, a, b):
    st = list(str(st))
    st[a],st[b]= st[b],st[a]
    return "".join(st)
