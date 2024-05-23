# Palindromik bir sayı her iki şekilde de aynı şekilde okunur.
# 2 basamaklı iki sayının çarpımından elde edilen en büyük palindrom 9009 = 91 × 99'dur.
#
# 3 basamaklı iki sayının çarpımından oluşan en büyük palindromu bulun.

polindromikSayilar=[]
for i in range(100,1000):
    for k in range(100,1000):
        c = i * k
        if str(c) == str(c)[::-1]:
            polindromikSayilar.append(c)
            print(i," x ",k," = ",c)

print("Sonuç :",max(polindromikSayilar))
