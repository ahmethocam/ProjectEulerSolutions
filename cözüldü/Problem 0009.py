import math
buldum = False
sayilar = ()
for a in range(1,1000):
    for b in range(a+1,1000):
        c2 = a**2 + b**2
        c = math.isqrt(c2)

        if c2 == c**2:
            if a+b+c == 1000:
                sayilar = (a,b,c,a*b*c)
                buldum=True
                break

    if buldum==True:
        print(sayilar)
        break



