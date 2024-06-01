import math
tler = []
t=0
print(math.sqrt(3*3+4*4))
if isinstance(math.sqrt(3*3+4*4),int):
    print (True)

for a in range(1,1001):
    for b in range(1,1001):
        c = math.sqrt(a*a+b*b)
        t = a + b + c
        if c.is_integer() and t<1001:
            tler.append([a,b,c,t])

for i in tler:
    print(i[0],i[1],i[2],i[3])

# Answer:  840
# Completed on Sat, 1 Jun 2024, 16:43

