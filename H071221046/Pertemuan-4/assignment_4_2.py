#Najwa Hanana
#H071221046
#PERTEMUAN 4

print()
def hitung_FPB(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            fpb = i
            
    return fpb
n1 = int(input('Masukkan Nilai 1 : '))
n2 = int(input('Masukkan Nilai 2 : '))
print()
print ('---Mencari Nilai FPB---')
print (f'FPB ({n1}, {n2}) : ', hitung_FPB(n1,n2))
print()