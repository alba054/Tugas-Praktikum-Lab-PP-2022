import os
import re

data = {
    'Nama' : None,
    'Email' : None,
    'Password' : None
    }

while True:
    print("="*50)
    print("Selamat Datang Silahkan Pilih Opsi Menu anda")
    print('''1. Detail Anda
2. Ubah Nama
3. Jumlah Data pada File
4. Save Data pada File
5. Buat Data Baru 
6. Keluar''')
    opsi = int(input("Silahkan Pilih Opsi Anda : "))
    print("="*50)

    if opsi == 1:
        if (data.get('Nama') and data.get('Email') and data.get('Password')) == None:
            print("Data saat ini kosong")
        else:
            print(f'''Data anda adalah
Nama : {data['Nama']}
Email : {data['Email']}
Password : {data['Password']} 
            ''')

    elif opsi == 2:
        if data.get('Nama') == None:
            print("Data saat ini kosong")
        else:
            data['Nama'] = input("Silahkan Input Nama Baru : ")

    elif opsi == 3:
        file = input("Silahkan Masukkan Nama File : ") + ".txt"
        target = os.path.isfile(file)
        if target == True:
            open_file = open(file, "r")
            read_data = open_file.read()
            banyak_data = read_data.lower().count("nama")
            print(f'''Berhasil
Jumlah Data Pada File : {banyak_data} Data''')
        else:
            print(f"Tidak Terdapat File dengan Nama {file}")
            print("Jumlah Data Pada File: 0 Data")

    elif opsi == 4:
        if (data.get('Nama') and data.get('Email') and data.get('Password')) == None:
            print("Data saat ini kosong")
        else:
            file = input("Silahkan Masukkan Nama file : ") + ".txt"
            target = os.path.isfile(file)
            if target == False:
                with open(file, "w") as target:
                    target.write("+" + "=" * 50)
                    target.write("\n|Data yang tersimpan")
                    target.write("\n+" + "=" * 50)
                    target.write("\n|Nama" + " " *12 + ": " + data.get('Nama'))
                    target.write("\n|Email" + " " *11 + ": " + data.get('Email'))
                    target.write("\n|Password" + " " *8 + ": " + data.get('Password'))
                    target.write("\n+" + "=" * 50)
                    data["nama"] = "kosong"
                    data["email"] = "kosong"
                    data["password"] = "kosong"

            else:
                with open(file, "a") as target:
                    target.write("\n|Nama" + " " *12 + ": " + data.get('Nama'))
                    target.write("\n|Email" + " " *11 + ": " + data.get('Email'))
                    target.write("\n|Password" + " " *8 + ": " + data.get('Password'))
                    target.write("\n+" + "=" * 50)
                    data["nama"] = "kosong"
                    data["email"] = "kosong"
                    data["password"] = "kosong"
            
    elif opsi == 5:
        data['Nama'] = input("Silahkan Masukkan Nama Anda : ")
        while True:
            email = input("Silahkan Masukkan Email Anda : ")
            if re.fullmatch(r'[a-z0-9]+@student[.]unhas[.]ac[.]id$', email): 
                data['Email'] = email
                break
            else: 
                print("Email yang anda Masukkan Salah")
        while True:
            password = input("Silahkan Masukkan Password Anda : ")
            if not re.fullmatch(r'[\w\s!@#$%^&*)():"><]{8,20}$', password):
                print("Password harus memiliki panjang 8 - 20 karakter")
            elif not re.findall(r'(?=.*[a-z])(?=.*[A-Z])(?=.*\d)', password):
                print("Password yang anda masukkan terlalu lemah, gunakan minimal 1 huruf kapital, huruf kecil, dan angka")
            else:
                data['Password'] = password
                break
            
    elif opsi == 6:
        print("Sampai Jumpa Lagi")
        quit()


            

