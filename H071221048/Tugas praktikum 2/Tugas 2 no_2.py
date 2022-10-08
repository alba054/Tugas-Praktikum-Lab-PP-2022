gol=(input("golongan ="))
daya = int(input("daya="))
pemakaian=int(input("pemakaian="))
tarif_1= 1352
tarif_2=1444.7
tarif_3=144.7
tarif_4=1699.53
tarif_5=1688.53
tarif_6=144.7
tarif_7=114.74
tarif_8=1314.12
tarif_9=1523.28
tagihan= daya*pemakaian
if gol =='R1' and daya ==900:
    tagihan=(pemakaian*tarif_1)/1000
elif gol=='R1' and daya == 1300:
    tagihan=(pemakaian*tarif_2)/1000
elif gol=='R1' and daya==2200:
    tagihan=(pemakaian*tarif_3)/1000
elif gol=='R2' and 3500<=daya <=5500:
    tagihan=(pemakaian*tarif_4)/1000 
elif gol=='R3' and daya>=6.600:
    tagihan=(pemakaian*tarif_5)/1000
elif gol=='B2' and 6600<=daya <=200000:
    tagihan=(pemakaian*tarif_6)/1000
elif gol=='B3' and daya>200000:
    tagihan=(pemakaian*tarif_7)/1000
elif gol=='I3' and daya>20000:
    tagihan=(pemakaian*tarif_8)/1000
elif gol=='P1' and 6600<=daya<=200000:
    tagihan=pemakaian*tarif_9
print(">Jumlah tagihan anda:",round(tagihan,2))