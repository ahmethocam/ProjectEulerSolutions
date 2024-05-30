from myTools import *

import math

import decimal
sonuclar= []
decimal.getcontext().prec = 1999
for i in range(1,1000):
    sonuc = decimal.Decimal(1)/decimal.Decimal(i)
    canon = decimal.getcontext().is_canonical(sonuc)
    saglama = sonuc * i
    if saglama != 1:
        sonuclar.append(f"{i}--" + str(sonuc)[3:])
for sonuc in sonuclar:
   print(sonuc)


# 438596491228070175
# 2673796791443850
# 258397932816537467700  1/387
# 023255813953488372093 1 / 43
# 149253731343283582089552238805970   //buldum ama giriş alanı yetmiyor
# 12048192771084337349397590361445783132530
# 409836065573770491803278688524590163934426229508196721311475