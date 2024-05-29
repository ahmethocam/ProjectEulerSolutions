import datetime

from myTools import *

start = datetime.datetime.now()
liste = [2]
for i in range(2,2000000):
    if TolgaAsalBulma(i):
        liste.append(i)
print(len(liste),sum(liste))
finish = datetime.datetime.now()
print("Süre :",finish-start)

#
# start = datetime.datetime.now()
# liste = []
# for i in range(2,100000):
#     if asalmi(i):
#         liste.append(i)
# print(len(liste),sum(liste),liste)
# finish = datetime.datetime.now()
# print("Süre :",finish-start)