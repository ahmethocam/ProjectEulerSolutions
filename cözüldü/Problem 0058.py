from myTools import *

kosesayisi = 1
for kenarSayisi in range(26201,99999,2):
    baslangic = 1
    koseler = []
    kosesayisi = 1
    asalkoseler = 0
    for kenar in range(3,kenarSayisi+1,2):
        koseler.append(baslangic+(kenar-1)*1)
        koseler.append(baslangic+(kenar-1)*2)
        koseler.append(baslangic+(kenar-1)*3)
        koseler.append(baslangic+(kenar-1)*4)
        kosesayisi += 4
        baslangic = baslangic+(kenar-1)*4
        for kose in koseler:
            if TolgaAsalBulma(kose):
                asalkoseler += 1
        koseler.clear()
    print("Kenar Sayısı = ",kenarSayisi,"-", asalkoseler,"/",kosesayisi,"=",asalkoseler/kosesayisi*100,"%")

# Answer:  26241
# Completed on Mon, 17 Jun 2024, 12:28