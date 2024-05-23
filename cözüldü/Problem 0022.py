# Using names.txt (right click and 'Save Link/Target As...'),
# a 46K text file containing over five-thousand first names,
# begin by sorting it into alphabetical order.
# Then working out the alphabetical value for each name,
# multiply this value by its alphabetical position in the list to obtain a name score.
#
# For example, when the list is sorted into alphabetical order,
# COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
# So, COLIN would obtain a score of 938 × 53 = 49714.
#
# What is the total of all the name scores in the file?

def harfSirasi(harf):
    harfler = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split()
    return harfler.index(harf) + 1


def harfSiralariToplami(isim):
    t = 0
    for i in isim:
        t +=harfSirasi(i)
    return t



f = open("p022_names.txt", "r")
isimler = sorted(f.read().split(","))
s= 0
sira = 0
toplam = 0
for isim in isimler:
    isim = isim.replace("\"","")
    sira += 1
    toplam += harfSiralariToplami(isim)  * sira

print (toplam)


