def rakamlarToplami(sayi):
    f=0
    for j in str(sayi):
        f +=int(j)
    return f

def birlerBasamagi(sayi):
    return int(str(sayi)[-1])

def sonBasamaklar(sayi,adet):
    if len(str(sayi))<=adet:
        return sayi
    return int(str(sayi)[-1*adet:])

def ilkBasamaklar(sayi,adet):
    if len(str(sayi))<=adet:
        return sayi
    return int(str(sayi)[:adet])


def terstenYaz(yazi):
    txt = str(yazi)[::-1]
    return txt


def asalSayilar(max=1000):
    asallar = []
    for i in range(2,max):
        asalDegil=False
        for k in range(2,i):
            if i % k == 0:
                asalDegil=True
                break
        if asalDegil==False:
            asallar.append(i)
    return asallar

def asalmi(sayi):
    asalDegil=False

    for k in range(2,sayi):
        if sayi % k == 0:
            asalDegil=True
            break
    return not asalDegil

