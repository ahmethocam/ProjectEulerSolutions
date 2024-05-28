import math
t=0
for n in range(1,101):
    for r in range(1,101):
        if n >= r:
            a = math.factorial(n) / (math.factorial(r)*(math.factorial(n-r)))
            if a > 1000000:
                t = t+1
print(t)