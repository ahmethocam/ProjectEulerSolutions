kacinci =0
for sayi in range(2,110000):
      sayac=0
      for k in range(2,sayi):
            if sayi % k == 0:
                  sayac = sayac+1
                  break
      if sayac == 0:
            kacinci +=1

      if kacinci == 10001:
            print(kacinci," : ",sayi)
            break
