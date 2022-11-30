print("Selamat datang untuk memulai silahkan input data anda ")

a = input("Input nama: ")
b = input("Input umur: ")
c = input("Input alamat: ")
d = input("Input Daerah asal: ")
e = input("Input asal SD: ")
f = input("Input asal SMP: ")
g = input("Input asal SMA: ")
h = input("Input hobby: ")

detail = {
    'nama': a,
    'umur': b,
    'alamat': c,
    'daerah asal': d,
    'SD': e,
    'SMP': f,
    'SMA': g,
    'hobby': h
    }

while True:
    print("=============================================================")
    print(f"Selamat datang {detail['nama']} silahkan pilih opsi")
    print("=============================================================")
    print('''1. Detail anda
    2. Ubah Nama
    3. Ubah Umur
    4. Ubah Alamat
    5. Ubah Daerah asal
    6. Ubah Asal SD
    7. Ubah Asal SMP
    8. Ubah Asal SMA
    9. Ubah hobby
    10. Keluar''')
    print("=============================================================")
    x = int(input("Input opsi: "))
    print("=============================================================")
    if x == 1:
        print(f'''Data anda adalah
    Nama: {detail['nama']}
    Umur: {detail['umur']}
    Alamat: {detail['alamat']}
    Daerah asal: {detail['daerah asal']}
    SD: {detail['SD']}
    SMP: {detail['SMP']}
    SMA: {detail['SMA']}
    Hobby: {detail['hobby']}''')
    elif x == 2:
        detail['nama'] = input("Silahkan input nama baru: ")
        print("Data anda sukses diperbarui")
    elif x == 3:
        detail['umur'] = input("Silahkan input umur baru: ")
        print("Data anda sukses diperbarui")
    elif x == 4:
        detail['alamat'] = input("Silahkan input alamat baru: ")
        print("Data anda sukses diperbarui")
    elif x == 5:
        detail['daerah asal'] = input("Silahkan input daerah asal baru: ")
        print("Data anda sukses diperbarui")
    elif x == 6:
        detail['SD'] = input("Silahkan input SD baru: ")
        print("Data anda sukses diperbarui")
    elif x == 7:
        detail['SMP'] = input("Silahkan input SMP baru: ")
        print("Data anda sukses diperbarui")
    elif x == 8:
        detail['SMA'] = input("Silahkan input SMA baru: ")
        print("Data anda sukses diperbarui")   
    elif x == 9:
        detail['hobby'] = input("Silahkan input hobby baru: ")
        print("Data anda sukses diperbarui")
    elif x == 10:
        print(f"Selamat Tinggal {detail['nama']}")
        quit()