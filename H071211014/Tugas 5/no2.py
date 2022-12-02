print("Selamat datang untuk memulai silahkan input data anda")
data={}
nama   = input("Input nama : ")
umur   = input("Input umur : ")
alamat = input("Input alamat : ")
data['nama'] = nama
data['umur'] = umur
data['alamat'] = alamat

while (True):
    print(50*"=")
    print(f"Selamat datang {nama} silahkan pilih opsi")
    print(50*"=") 
    print("1. Detail anda")
    print("2. Ubah nama")
    print("3. Ubah umur")
    print("4. Ubah alamat")
    print("5. Keluar")
    print(50*"=")
    opsi = int(input("Input Opsi : "))
    print(50*"=")
    if opsi == 1 :
        print(f"Data anda adalah : ")
        print("Nama : ", data['nama'])
        print("Umur : ", data['umur'])
        print("Alamat : ", data['alamat'])
        print(50*"=")
    elif opsi == 2 :
        nama = input("Silahkan Input nama baru : ")
        data["nama"] = nama
        print("Data anda sukses di diperbarui")
        print(50*"=")
    elif opsi == 3 :
        umur = input("Silahkan Input umur baru : ")
        data ["umur"] = umur
        print("Data anda sukses di diperbarui")
        print(50*"=")
    elif opsi == 4:
        alamat = input("Silahkan Input alamat baru : ")
        data ["alamat"] = alamat
        print("Data anda sukses di diperbarui")
        print(50*"=")
    else:
        opsi == 5
        print(f"Selamat Tinggal {nama}")
        break