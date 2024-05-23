
def bolenToplami(sayi):
    t=0
    for i in range(1,sayi):
        if sayi % i==0:
            t +=i
    return t
    
    
t=0

for i in range(1,10000):
    
    s=bolenToplami(i)
   
    if i==bolenToplami(s):
        t+=i
        print("------",i,s)
    
print(t)
    