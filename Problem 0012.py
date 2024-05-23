for i in range(110000,210000):
    toplam = i*(i+1)/2
    say=0
    for k in range(1,int(toplam // 2)):
       if (toplam % k == 0):
           say +=1
    if say > 150:
        print(i,"-",toplam," : ",say)

