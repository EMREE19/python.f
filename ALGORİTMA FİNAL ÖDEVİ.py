#soru1
#Benım öğrenici numaram 03 olduğu için çalıştırırken kodu hata aldım ben de o yüzden 2 ve 50 arasında ki asal sayıları gösterdim
for i in range(2,50):
    emre = False
    for j in range(2, i):
            if (i % j) is 0:
                emre=True
    if emre is False:
        print (i)


#Soru 3
A=[[1,2,-1],
    [2,5,2],
    [-1,-2,2]]
for i in range(3):
   print(A[i])
isim=[[5,13,18],
   [5,5,18],
   [4,5,13]]
print()
for i in range(3):
   print(isim[i])
print()
sifre=[[0,0,0],
   [0,0,0],
   [0,0,0]]
for e in range(len(A)):
    for m in range(len(isim[0])):
        for r in range(len(isim)):
            sifre[e][m] +=A[e][r]*isim[r][m]
for sifre in sifre:
    print(sifre)


#Soru 4
from datetime import datetime

e = gün = int(input('Günü giriniz : '))
m = ay = input('Ayı giriniz : ')
r = yıl = int(input('Yılı giriniz : '))
e = date1 = datetime.date(gün , ay , yıl)
print("datetime.date(gün, ay, yıl)")
