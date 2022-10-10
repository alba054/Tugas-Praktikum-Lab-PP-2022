#Najwa Hanana
#H071221046
#PERTEMUAN 4

print()
print ('--Faktorial--')
def faktorial (nilai) :
    if nilai == 1 :
        return (nilai)
    else :
        return (nilai*faktorial(nilai-1))

angka = int(input('Masukkan Angka : '))
print ("%d! = %d" % (angka, faktorial(angka)))

print()