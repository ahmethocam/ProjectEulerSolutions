t = 0
toplamlar = []
for a in range(1,100):
    for b in range(1,100):
        k = str(a**b)
        for l in k:

            t = t + int(l)
        print(k, t)
        toplamlar.append(t)
        t=0

print(max(toplamlar))
