# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once;
# for example, the 5-digit number, 15234, is 1 through 5 pandigital.
#
# The product 7254 is unusual, as the identity, 39 × 186 = 7254,
# containing multiplicand, multiplier, and product is 1 through 9 pandigital.
#
# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
#
# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
#


def kontrolEt(txt):
    rakamlar = "1 2 3 4 5 6 7 8 9".split()
    cop = False
    if len(txt)==9:
        for j in rakamlar:
            if j not in txt:
                cop = True
                break
    else:
        cop=True

    return not cop

t = []
toplam=0
for i in range(1, 100):
    for k in range(100, 10000):
        c = i * k
        txt = str(i) + str(k) + str(c)

        if kontrolEt(txt) == True:
            print(i, " x ", k, " = ", c, "=", txt)
            if str(c) not in t:
                t.append(c)
for k in set(t):
    toplam += k
print ("Cevap: " ,toplam)
