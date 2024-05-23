son = 1001*1001

bas= 1
kose=1
artis=2
t=1
while bas<son:
    for i in range(4):
        bas=bas+ artis
        print (bas)
        t+=bas
    artis+=2
print (t)

    