golongan = str(input('golongan :'))
daya = float(input('daya : '))
tarif = float(input('tarif : '))

if golongan=='R1' :
    if daya==900 :
        print (f'jumlah tagihan anda : {tarif*1352}')
    elif daya>=1300 and daya<=2200 :
        print (f'jumlah tagihan anda : {tarif*1444.70}')
elif golongan=='R2' :
    if daya>=3500 and daya<=5500 :
        print (f'jumlah tagihan anda : {tarif*1699.53}')
elif golongan== 'R3' :
    if daya>=6600 : 
        print (f'jumlah tagihan anda : {tarif*1699.53}')
elif golongan=='B2' :
    if daya>=6600 and daya<=200000 :
        print (f'jumlah tagihan anda : {tarif*1444.70}')
elif golongan=='B3' :
    if daya>200000 :
        print (f'jumlah tagihanb anda : {tarif*1114.74}')
elif golongan=='I3' :
    if daya>=200000 :
        print (f'jumlah tagihan anda : {tarif*1314.12}')
elif golongan=='P1' :
    if daya>=6600 and daya<=200000 :
        print (f'jumlah tagihan anda : {tarif*1523.28}')
