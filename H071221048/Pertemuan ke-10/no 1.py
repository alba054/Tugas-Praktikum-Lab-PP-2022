import re
import os

while True:
    print("""Selamat datang Silahkan Pilih Opsi Menu Anda :
    1. Detail Anda
    2. Ubah Nama
    3. Jumlah Data Pada File
    4. Save Data Pada File
    5. Buat Data Baru
    6.Keluar""" )

    O=int(input("Silahkan pilih opsi anda : "))


    
    if O==1:
        try:
            print(f"""Data anda adalah:
            Nama     : {n}
            Email    : {e}
            password :{p}""")
        except:
            print("Data saat ini kosong")
    
    elif O==2:
        n=input("Silahkan Input Nama Baru : ")
    
    elif O==3:
        try:
            print(f"Jumlah data yang tersimpan {jml}")
        
        except:
            print("Data saat ini kosong")
        

    elif O==4:
        nf=input("Silahkan Masukkan nama File : ")
        nfl=f'D:\File Kampus\Praktikum pemograman\Tugas\Tugas Praktikum 10\{nf}.txt'
        nfl= os.path.exists(nfl)

        if nfl==True:
            f=open (f"{nf}.txt","a")
            f.write(f"""
    | Nama : {n}
    | Email : {e}
    | Password : {p}
+{"="*40}""")
            f.close()
            jml+=1
        elif nfl==False:
            f=open (f"{nf}.txt","w")
            f.write(f"""+{"="*40}
|Data Yang tersimpan :
+{"="*40}
    | Nama : {n}
    | Email : {e}
    | Password : {p}
+{"="*40}""")
            f.close()
            jml=1

    elif O==5:
        while True:
            n=input("Masukkan nama Anda:")
            e=input("Silahkan Masukkan Email Anda : ")
            patternp = r"[\da-z]+(@student.unhas.ac.id)"
            result=re.match(patternp,e)
            if result:
                p=input("Silahkan Masukkan Password Anda : ")
                patternp = r".{8,20}"
                result=re.match(patternp,p)
                if result:
                    patternp=r"([a-z][A-Z]\d|[a-z]\d[A-Z]|[A-Z][a-z]\d|[A-Z]\d[a-z]|\d[a-z][A-Z]|\d[A-Z][a-z])+"
                    result=re.match(patternp,p)
                    if result:
                        print("Berhasil")
                        break
                    else:
                        print("""Password yang anda masukkan terlalu lemah, gunakan minimal 1 
                            huruf kapital, huruf kecil, dan angka""")
                else:
                    print("password harus memiliki Panjang 8-20 Karakter")    
    
            else:
                print("email yang Anda Masukkan Salah ")        
    elif O==6:
        print("Sampai Jumpa Lagi")
        break