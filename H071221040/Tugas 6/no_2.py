nama_file = input('Masukkan nama file: ')
salinan = input('Masukkan nama file salinan: ')

try :
    with open(f"{nama_file}.txt", "r") as file_asli :
        baca = file_asli.read()
except :
    print('\nGagal')
else :
    with open (f"{nama_file}.txt") as garis :
        rata_kanan = garis.readlines()
    with open (f"{salinan}.txt","w") as ind :
        for i in rata_kanan :
            ind.write(i.rjust(40))
    print("\nBerhasil")

    