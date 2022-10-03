#Najwa Hanana
#H071221046
#Pertemuan 2


print ('            ---Tarif Tagihan Listrik---'                )
print ('-------------------------------------------------------')
print ('|   Golongan  |        Daya         |    Tarif/kWh    |')
print ('| ------------|---------------------|---------------- |')
print ('|      R1     | 900 VA              | Rp.1.352/kWh    |')
print ('|      R1     | 1.300 VA            | Rp.1.444,70/kWh |')
print ('|      R1     | 2.200 VA            | Rp.1.444,70/kWh |')
print ('|      R2     | 3.500 VA -5500 VA   | Rp.1.699,53/kWh |')
print ('|      R3     | 6.600 VA - ke atas  | Rp.1.699,53/kWh |')
print ('|      B2     | 6.600 VA - 200kVA   | Rp.1.444,70/kWh |')
print ('|      B3     | Di atas 200 kVA     | Rp.1.114,74/kWh |')
print ('|      I3     | 200 kVA - ke atas   | Rp.1.314,12/kWh |')
print ('|      P1     | 6.600 VA - 200 kVA  | Rp.1.523,28/kWh |')
print ('-------------------------------------------------------')


gol = input('Golongan : ')
daya = float(input('Daya : '))
pemakaian = float(input('Pemakaian : '))
tarif = pemakaian/1000

a = ('R2')
b = ('R3')
c = ('B2')
d = ('B3')
e = ('I3')
f = ('P1')

if daya <= 900 :
    R1a = tarif*1352
    print ('Jumlah Tagihan Anda :',round(R1a,4))

elif daya <= 1300 :
    R1b = tarif*1444.70
    print ('Jumlah Tagihan Anda :',round(R1b,4))

elif daya <= 2200 :
    R1c = tarif*1444.70
    print ('Jumlah Tagihan Anda :',round(R1c,4))

if gol == a :
    R2 = tarif*1699.53
    print ('Jumlah Tagihan Anda :',round(R2,4))

elif gol == b :
    R3 = tarif*1699.53
    print ('Jumlah Tagihan Anda :',round(R3,4))

elif gol == c :
    B2 = tarif*1444.70
    print ('Jumlah Tagihan Anda :',round(B2,4))

elif gol == d :
    B3 = tarif*114.74
    print ('Jumlah Tagihan Anda :',round(B3,4))

elif gol == e :
    I3 = tarif*1314.12
    print ('Jumlah Tagihan Anda :',round(I3,4))

elif gol == f :
    P1 = tarif*1523.28
    print ('Jumlah Tagihan Anda :',round(P1,4))

else :
    print ('Data Tidak Valid')