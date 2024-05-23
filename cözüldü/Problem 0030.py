bas=10
t=0
gt=0
for i in range(bas,10000000):
    t=0
    
    for k in str(i):
        t+=int(k)**5
    if i == t:
        gt+=i
        print(i)
print(gt)
