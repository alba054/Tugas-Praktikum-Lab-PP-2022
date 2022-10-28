nama_file = input('Masukkan Nama File: ')
jumlah_asisten = int(input('Masukkan Jumlah Asistensi'))
try :
    with open (f"{nama_file}.txt","w") as table:
        table.write(f"+{'-'*20}+{'-'*15}+{'-'*10}+\n")
        table.write(f"|NAMA{' '*16}|{' ' *15}|ANGKATAN{' '*2}|\n")
        table.write(f"+{'-'*20}+{'-'*15}+{'-'*10}+\n")
        for i in range(jumlah_asisten) :
            nama_asisten = input("Nama asisten: ")
            ganti = nama_asisten.replace(' ','_')
            NIM = input("NIM: ")
            angkatan = input("Angkatan: ")
            if len(nama_asisten) <= 20 and len(NIM) <= 15 and len(angkatan) <=10 :
                table.write(f"|{ganti}{' '*(20-len(ganti))}|{NIM}{' '*(15-len(NIM))}|{angkatan}{' '*(10-len(angkatan))}|\n")
            else :
                print("Inputa Tidak Boleh Melewati Batas")
                raise Exception ()
        table.write(f"={'-'*20}+{'-'*15}+{'-'*10}+\n")
        print("Berhasil")
except :
    print("Gagal")
        