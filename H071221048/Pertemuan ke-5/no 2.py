print("Selamat datang ,untuk memulai silahkan menginput nama anda")
n=input("Input nama :")
u=input("Input umur :")
a=input("Input alamat :")
print("="*75)
print(f"Selamat datang {n},silahkan pilih opsi")
print("="*75)
print('''
1.Detail anda
2.Ubah nama
3.Ubah umur
4.Ubah alamat
5.Keluar
''')

mydict={
    "nama":n,
    "umur":u,
    "alamat":a}


def dictionary(s):
    if s==1:
        for x,y in mydict.items():
            print(f"{x} : {y}")
        s=int(input("Input opsi : "))
        dictionary (s)
    elif s ==2:
        n=input("Silahkan input nama baru : ")
        print("Data anda sukses diperbarui")
        mydict.update({"nama":n})
        s=int(input("Input opsi : "))
        dictionary (s)
    elif s== 3:
        u=input("Silahkan input umur baru : ")
        print("Data anda sukses diperbarui")
        mydict.update({"umur":u})
        s=int(input("Input opsi : "))
        dictionary (s)
    elif s==4:
        a=input("Silahkan input alamat baru : ")
        print("Data anda sukses diperbarui")
        mydict.update({"alamat":a})
        s=int(input("Input opsi : "))
        dictionary (s)
    elif s==5:
        print("Selamat tinggal",mydict.get("nama"))
    else:
        try:
            print("Opsi inputan salah")
            s=int(input("Input opsi : "))
            dictionary (s)
        except:
            print("Inputan harus berupa angka")
            dictionary (s)
    



print("="*75)
try:
    s=int(input("input opsi :"))
    dictionary(s)
except:
    print("Inputan harus berupa angka")
  
print("="*75)



