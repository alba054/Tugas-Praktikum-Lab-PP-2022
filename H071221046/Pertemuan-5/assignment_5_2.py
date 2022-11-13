#Najwa Hanana
#H071221046

print ('Selamat Datang, Untuk Memulai Silahkan Input Data Anda')
name = input('Input nama : ')
age = input('Input usia : ')
adress = input('Input alamat : ')

listName = []
listName.append(name)
listAge = []
listAge.append(age)
listAdress = []
listAdress.append(adress)

k = 0
while k >= 0 :
    def equals(a) :
        for i in range(a) :
            print('=', end = '')

    k += 1
    equals(100)
    if k == 1 :
        print(f'\nSelamat Datang {name}, silahkan pilih opsi')
    elif k > 1 :
        print(f'\nSelamat Datang {listName[0]}, silahkan pilih opsi')

    equals(100)
    print('\n1. Detail anda')
    print('2. Ubah Nama')
    print('3. Ubah Umur')
    print('4. Ubah Alamat')
    print('5. Keluar')
    equals(100)

    option = int(input('\nInput opsi : '))
    equals(100)

    if option == 1 :
        print('\nData anda adalah')
        print(f'Nama   : {listName[0]}')
        print(f'Umur   : {listAge[0]}')
        print(f'Alamat : {listAdress[0]}')

    elif option == 2 :
        newName = input('\nSilahkan input nama baru : ')
        listName.clear()
        listName.append(newName)
        print('Data anda sukses untuk diperbarui')

    elif option == 3 :
        newAge = int(input('\nSilahkan input umur baru : '))
        listAge.clear()
        listAge.append(newAge)
        print('Data anda sukses untuk diperbarui')

    elif option == 4 :
        newAdress = input('\nSilahkan input alamat baru : ')
        listAdress.clear()
        listAdress.append(newAdress)
        print('Data anda sukses untuk diperbarui')

    elif option == 5 :
        print(f'\nSelamat Tinggal {listName[0]}')
        break