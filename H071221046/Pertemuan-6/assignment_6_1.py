#Najwa Hanana
#H071221046

try :
    c = input()
    b = input()
    with open (c+'.txt', 'r') as file :
        a = file.read()


    with open (b+'.txt', 'w') as file :
        file.write(a)

    print ('Berhasil')

except :
    print ('Gagal')
