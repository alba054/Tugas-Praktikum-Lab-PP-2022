# data_orang = {}
nama = input("input nama: ")
umur = input("input umur: ")
alamat = input("input alamt: ")
daerah_asal = input("input daerah asal: ")
sd = input("input sd: ")
smp = input("input smp: ")
sma = input("input sma: ")

data_orang = {
    "nama": nama ,
    "umur":umur,
    "alamat":alamat,
    "daerah asal":daerah_asal,
    "sd":sd,
    "smp":smp,
    "sma":sma,
    "hobby":[],
}
print("Selamat datang untuk memulai silahkan input data anda")
#data_orang["nama"] = input("Input Nama: ")
#data_orang["umur"] = input("Input Umur: ")
#data_orang["alamat"] = input("Input Alamat: ")
#data_orang["daerah asal"] = input("Input daerah asal: ")
#data_orang["sd"] = input("Input sd: ")
#data_orang["smp: "] = input("Input sd: ")
#data_orang["sma: "] = input("input sma: ")
#data_orang["hobby: "] = input("input hobby: ")

while True:
    print("=====================================================")
    print("Selamat Datang", nama, "Silahkan Pilih Opsi")
    print("=====================================================")
    print("1. Detal Anda")
    print("2. Ubah Nama")
    print("3. Ubah Umur")
    print("4. Ubah Alamat")
    print("5. ubah daerah asal")
    print("6. ubah sd")
    print("7. ubah smp")
    print("8. ubah sma")
    print("9. tambah hobby")
    print("10. Keluar")
    print("=====================================================")

    a = int(input("Input Opsi"))
    print("=====================================================")
    if a == 1:
        print("Data Anda Adalah")
        print("Nama:",data_orang["nama"])
        print("Umur:",data_orang["umur"])
        print("Alamat:",data_orang["alamat"])
        print("Daerah asal:",data_orang["daerah asal"])
        print("sd:",data_orang["sd"])
        print("smp:",data_orang["smp"])
        print("sma:",data_orang["sma"])
        print("hobby:",data_orang["hobby"])
    elif a == 2:
        ubah_nama = input("silahkkan input nama baru: ")
        data_orang["nama"] = ubah_nama
        print("Data Anda Sukses Diperbarui")
        print("=====================================================")
        print("Selamat Datang", nama, "Silahkan Pilih Opsi")
    elif a == 3:
        ubah_umur = input("silahkkan masukkan umur baru: ")
        data_orang["umur"] = ubah_umur
        print("Data Anda Sukses Diperbarui")
        print("=====================================================")
        print("Selamat Datang", nama, "Silahkan Pilih Opsi")
    elif a == 4:
        ubah_alamat = input("silahkkan masukkan daerah asal baru: ")
        data_orang["alamat"] = ubah_alamat
        print("Data Anda Sukses Diperbarui")
        print("=====================================================")
        print("Selamat Datang",nama, "Silahkan Pilih Opsi")
    elif a == 5:
        ubah_daerah_asal = input("silahkkan masukkan daerah asal baru: ")
        data_orang["daerah asal"] = ubah_daerah_asal
        print("Data Anda Sukses Diperbarui")
        print("=====================================================")
        print("Selamat Datang",nama , "Silahkan Pilih Opsi")
    elif a == 6:
        ubah_sd = input("silahkkan masukkan sd baru: ")
        data_orang["sd"] = ubah_sd
        print("Data Anda Sukses Diperbarui")
        print("=====================================================")
        print("Selamat Datang",nama, "Silahkan Pilih Opsi")
    elif a == 7:
        ubah_smp = input("silahkkan masukkan smp baru: ")
        data_orang["smp"] = ubah_smp
        print("Data Anda Sukses Diperbarui")
        print("=====================================================")
        print("Selamat Datang",nama, "Silahkan Pilih Opsi")
    elif a == 8:
        ubah_sma = input("silahkkan masukkan smp baru: ")
        data_orang["smp"] = ubah_sma
        print("Data Anda Sukses Diperbarui")
        print("=====================================================")
        print("Selamat Datang",nama, "Silahkan Pilih Opsi")
    elif a == 9:
        tambah_hobby = input("silahkkan masukkan hobby  baru: ")
        data_orang["hobby"].append(tambah_hobby)
        print("Data Anda Sukses Diperbarui")
        print("=====================================================")
        print("Selamat Datang",nama, "Silahkan Pilih Opsi")