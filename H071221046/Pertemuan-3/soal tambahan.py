#Najwa Hanana
#H071221046
#Pertemuan 2

print ('---Cek Nilai---')

# pertemuan 3
''' 
    input nya sampe bener
    misal :
    Nilai : t
    Nilai : q
    Nilai : 91
    Nilai A
'''

nilai = 0
while True:
    try :
        nilai = int(input('Nilai    : '))
        if nilai >= 90 :
            print ('Nilai', nilai, '= A')
            print ('------')
        elif nilai >= 80 :
            print ('Nilai', nilai,'= B')
            print ('------')
        elif nilai >= 70 :
            print ('Nilai', nilai,'= C')
            print ('------')
        elif nilai >= 60 :
            print ('Nilai', nilai,'= D')
            print ('------')
        elif nilai >= 40 :
            print ('Nilai', nilai,'= E')
            print ('------')
        elif nilai < 40 :
            print ('Nilai', nilai,'= F')
            print ('------')
        
        break

    except :
            print ('Harap Masukkan Angka')
            print ('------')



# n = 9
# n % 3 == 0 # n habis dibagi 3

# if n % 3 == 0 :
#     print("habis dibagi 3")
# elif n % 3 != 0 :
#     print("tidak habis dibagi 3")

# if n > 1 :
#     print("lebih dari 1")

# if n > 5 :
#     print("lebih besar dari 5")
# elif n > 3 :
#     print("lebih besar dari 3")
# else :
#     print("lebih besar dari 2 atau sama dengan 2")

#