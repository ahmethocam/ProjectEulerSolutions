
for sayi in range(10000):
    s1 = sayi * 1
    s2 = sayi * 2
    s3 = sayi * 3
    s4= sayi * 4
    s5 = sayi * 5
    rakamlar = "123456789"

    s = str(s1) + str(s2)+ str(s3)+ str(s4)+ str(s5)
    sonuc = True
    if len(s) == 9:
        for i in rakamlar:

            if i in s:
                pass
            else:
                sonuc = False

                break
    else:
        sonuc = False


    if sonuc == True:
        print("Doğru Sonuç : ", sayi, s)

"""
Doğru Sonuç :  918273645    5
Doğru Sonuç :  192384576    3
Doğru Sonuç :  219438657    3
Doğru Sonuç :  273546819    3
Doğru Sonuç :  327654981    3

Doğru Sonuç :  672913458
Doğru Sonuç :  679213584
Doğru Sonuç :  692713854
Doğru Sonuç :  726914538
Doğru Sonuç :  729314586
Doğru Sonuç :  732914658
Doğru Sonuç :  769215384
Doğru Sonuç :  792315846
Doğru Sonuç :  793215864
Doğru Sonuç :  926718534
Doğru Sonuç :  927318546
Doğru Sonuç :  932718654
"""
