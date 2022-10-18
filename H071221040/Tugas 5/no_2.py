print('Selamat datang untuk memulai input data anda')
nama = input('Input nama: ')
umur = int(input('Input umur: '))
alamat = input('Input alamat: ')
daerah_asal = input('Input daerah asal: ')
sd = input('Input sd: ')
smp = input('Input smp: ')
sma = input('Input sma: ')

dict_profile = {
    'nama' : nama,
    'umur' : umur,
    'alamat' : alamat,
    'daerah asal' : daerah_asal,
    'sd' : sd,
    'smp' : smp,
    'sma' : sma,
    'hobi': []
}

while True :
    print('='*60)
    print(f"Selamat datang {dict_profile['nama']}, silahkan pilih opsi")
    print('='*60)
    print('1. Detail anda')
    print('2. Ubah nama')
    print('3. Ubah umur')
    print('4. Ubah alamt')
    print('5. Ubah daerah asal')
    print('6. Ubah sd')
    print('7. Ubah smp')
    print('8. Ubah sma')
    print('9. Tambah hobi')
    print('10. Keluar')
    print('='*60)

    opsi = input('Input opsi: ')

    print('='*60)
    if opsi=='1' :
        print('Data anda adalah')
        print(f"Nama : {dict_profile.get('nama')}")
        print(f"Umur : {dict_profile.get('umur')}")
        print(f"Alamat : {dict_profile.get('alamat')}")
        print(f"Daerah asal : {dict_profile.get('daerah asal')}")
        print(f"SD : {dict_profile.get('sd')}")
        print(f"SMP : {dict_profile.get('smp')}")
        print(f"Hobi : {dict_profile.get('hobi')}")
    elif opsi=='2' :
        ubah_nama = input('Silahkan input nama baru: ')
        dict_profile['nama']= ubah_nama
        print('Data anda sukses diper barui')
    elif opsi=='3' :
        ubah_umur = input('Silahkan input umur baru: ')
        dict_profile['umur']= ubah_umur
        print('Data anda sukses diper barui')
    elif opsi=='4' :
        ubah_alamat = input('Silahkan input alamat baru: ')
        dict_profile['alamat']= ubah_alamat
        print('Data anda sukses diper barui')
    elif opsi=='5' :
        ubah_daerah_asal = input('Silahkan input daerah asal baru: ')
        dict_profile['daerah asal']= ubah_daerah_asal
        print('Data anda sukses diper barui')
    elif opsi=='6' :
        ubah_sd = input('Silahkan input sd baru: ')
        dict_profile['sd']= ubah_sd
        print('Data anda sukses diper barui')
    elif opsi=='7' :
        ubah_smp = input('Silahkan input smp baru: ')
        dict_profile['smp']= ubah_smp
        print('Data anda sukses diper barui')
    elif opsi=='8' :
        ubah_sma = input('Silahkan input sma baru: ')
        dict_profile['sma']= ubah_sma
        print('Data anda sukses diper barui')
    elif opsi=='9' :
        tambah_hobi = input('Silahkan input hobi baru: ')
        dict_profile['hobi'].append(tambah_hobi) 
        print('Data anda sukses diper barui')
    elif opsi=='10' :
        print(f"Selamat tinggal {dict_profile['nama']}")
        break
    else :
        print('Opsi salah')
