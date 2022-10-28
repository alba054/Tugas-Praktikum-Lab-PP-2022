print("selamat datang untuk memulai silahkan input data anda")

nama=input("input nama")
umur=input("input umur")
alamat=input("input alamat")
daerah_asal=input("input daerah asal")
SD=input("input SD")
SMP=input("input SMP")
SMA=input("input SMA")
Hobby=input("input Hobby")

data = {
    "nama" : nama,
    "umur" : umur,
    "alamat" : alamat,
    "daerah_asal" : daerah_asal,
    "SD" : SD,
    "SMP" : SMP,
    "SMA" : SMA,
    "Hobby" : Hobby 
}
while True :
    print("==========================================")
    print("selamat datang fatwa anugrah silahkan pilih obsi")
    print("===============================================")


    print("1. Detail anda")
    print("2. Ubah nama")
    print("3. Ubah umur")
    print("4. Ubah alamat")
    print("5. daerah asal")
    print("6. SD")
    print("7. SMP")
    print("8. SMA")
    print("9. Hobby")
    print("10. Keluar")
    print("==============================")

    opsi =int(input("input opsi"))

    if opsi==1:
        print("Data anda")
        print(f"Nama : {nama}")
        print(f"Umur : {umur}")
        print(f"Alamat : {alamat}")
        print (f"daerah asal : {daerah_asal}")
        print (f"SD : {SD}")
        print (f"SMP : {SMP}")
        print (f"SMA : {SMA}")
        print (f"Hobby : {Hobby}")

        print("===================================================")

    elif opsi==2 : 
        data ["nama"] = input ("silahkan input nama baru :")
        print("data anda sukses diperbarui")
    elif opsi==3 :
        data ["umur"] = input("silahkan input umur baru :")
        print ("data anda sukses diperbarui")
    elif opsi==4 :
        data ["alamat"] = input ("silahkan input alamat baru :")
        print ("data anda sukses diperbarui")
    elif opsi ==5 :
        data ["daerah asal"] = input ("silahkan masukkan daerah asal baru :")
        print ("data anda sukses diperbarui")
    elif opsi==6 :
        data ["SD"] = input ("silahkan input SD baru :")
        print ("data anda sukses diperbarui")
    elif opsi==7 :
        data["SMP"] = input ("silahkan input SMP baru :")
        print ("data anda sukses diperbarui")
    elif opsi==8 :
        data ["SMA"] = input("silahkan masukkan SMA baru :")
        print ("data anda sukses diperbarui")
    elif opsi==9 :
        data ["Hobby"] = input("silahkan masukkan Hobby :")
        print ("data anda sukses diperbarui")
    elif opsi==10 : 
        print("selamat tinggal")
        quit()
    

    

    





