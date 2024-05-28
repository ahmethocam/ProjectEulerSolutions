for sayi in range(100000,1000000):
    sayix2 = sayi*2
    sayix3 = sayi*3
    sayix4 = sayi*4
    sayix5 = sayi*5
    sayix6 = sayi*6
    ok=True
    for digit in str(sayi):
        if not(digit in str(sayix2) and digit in str(sayix3) and digit in str(sayix4) and digit in str(sayix5) and digit in str(sayix2)):
            ok = False
    if ok==True:
        print(sayi,sayix2,sayix3,sayix4,sayix5,sayix6)

# 142857 285714 428571 571428 714285 857142

