angka = list(input('masukkan angka : ').split())
    
for i in range(len(angka)):
    angka[i] = int(angka[i])
try :    
    angka_ganjil = sum(1 for i in angka if i%2!=0)
    angka_genap = sum(1 for i in angka if i%2==0 and i!=0)
    angka_positif = sum(1 for i in angka if i>0)
    angka_negatif = sum(1 for i in angka if i<0)
    angka_nol = sum(1 for i in angka if i==0)
    print (f'{angka_genap} angka genap')
    print (f'{angka_ganjil} angka ganjil')
    print (f'{angka_positif} angka positif')
    print (f'{angka_negatif} angka negatif')
    print (f'{angka_nol} angka nol')

except :
    print ('Inputan tidak falid')