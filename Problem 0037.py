from myTools import *


asallar = asalSayilar(100000)
t=0
for i in asallar:
    uyumlu = True
    if i > 10 :
        k = len(str(i))
        while k >= 1:
            ib = int(ilkBasamaklar(str(i),k))
            sb = int(sonBasamaklar(str(i),k))

            # print(k,"\t\t",ib,"\t\t",sb)
            k-=1
            # if ib not in asallar or sb not in asallar:
            if not asalmi(ib) or not asalmi(sb):
                uyumlu = False
                break

        if uyumlu==True:
            t+=i
            print ("-------------------",i)

print("Sonuç: ",t)
