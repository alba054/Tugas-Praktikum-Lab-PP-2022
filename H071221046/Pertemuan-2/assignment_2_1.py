#Najwa Hanana
#H071221046
#Pertemuan 2

print ('---Cek Nilai---')

nilai = 0
try :
    nilai = int(input('Nilai : '))
except :
    #print('Nilai Tidak Tertera')
    nilai = int(input('Nilai : '))

if nilai >= 90 :
    print ('Nilai', nilai, '= A')
elif nilai >= 80 :
    print ('Nilai', nilai,'= B')
elif nilai >= 70 :
    print ('Nilai', nilai,'= C')
elif nilai >= 60 :
    print ('Nilai', nilai,'= D')
elif nilai >= 40 :
    print ('Nilai', nilai,'= E')
elif nilai < 40 :
    print ('Nilai', nilai,'= F')

n = 9