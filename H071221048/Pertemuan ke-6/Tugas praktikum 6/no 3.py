from tabulate import tabulate
a=input("Masukkan nama file : ")
f=open(f"{a}.txt","w")
b=int(input("Masukkan jumlah asisten : "))
A=[]
B=[]
C=[["Nama","NIM","Angkatan"]]
for i in range(b):
    nama=input("Nama : ")
    NIM=input("NIM : ")
    ang=input("Angkatan : ")
    A.append(nama)
    A.append(NIM)
    A.append(ang)
    B=A.copy()
    C.append(B)
    A.clear()
print(C)
print(tabulate(C, headers="firstrow", tablefmt="psql"))
f.write(tabulate(C, headers="firstrow", tablefmt="psql"))
f.close()
print("Berhasil")