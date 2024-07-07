say = 0
k = 0
buldu = False
for s in range(0, 10000):
    for i in range(50):
        s = s + int(str(s)[::-1])
        if s == int(str(s)[::-1]):
            say = say + 1
            break
print("Çözün",10000-say)
# Answer:  249
# Completed on Sat, 8 Jun 2024, 12:35