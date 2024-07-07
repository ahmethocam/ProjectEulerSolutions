
tri,squ,pen,hex,hep,oct = [],[],[],[],[],[]
for n in range(1000):
    if len(str(int(n*(n+1)/2))) == 4:
        tri.append(str(int(n*(n+1)/2)))

    if len(str(n*n)) == 4:
        squ.append(str(n*n))

    if len(str(int(n*(3*n-1)/2))) == 4:
        pen.append(str(int(n*(3*n-1)/2)))

    if len(str(int(n*(2*n-1)))) == 4:
        hex.append(str(int(n*(2*n-1))))

    if len(str(int(n*(5*n-3)/2))) == 4:
        hep.append(str(int(n*(5*n-3)/2)))

    if len(str(n*(3*n-2))) == 4:
        oct.append(str(n*(3*n-2)))

print(len(tri),len(squ),len(pen),len(hex),len(hep),len(oct))
# print(tri[0],tri[0][2:4])

for tr in tri:
    for pn in squ:
        # print(tr,sq)
        for sq in pen:
            # for hx in hex:
            #     for hp in hep:
            #         for oc in oct:
            if tr[2:4]== sq[0:2] and sq[2:4]== pn[0:2] and pn[2:4] == tr[0:2]:
                print(tr,sq,pn)
