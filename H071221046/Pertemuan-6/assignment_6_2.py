#Najwa Hanana
#H071221046

try :
    c = input()
    b = input()
    with open (c+'.txt', 'r') as file :
        a = file.readlines()

        a[-1] = a[-1]+'\n'
        
    with open (b+'.txt', 'w') as file :
        for i in (a) :
            file.write(f"{i :>20}")

    print ('Berhasil')

except :
    print ('Gagal')