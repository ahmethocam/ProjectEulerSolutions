say = 0
k = 0
buldu = False
for s in range(10, 10000):
    while k < 100000:
        k = s
        ts = int(str(s)[::-1])
        tst = s + ts
        if tst == int(str(tst)[::-1]):
            buldu = True
            s = s + 1
            continue
        else:
            s = tst
    if not buldu:
        say = say + 1

print(say)
