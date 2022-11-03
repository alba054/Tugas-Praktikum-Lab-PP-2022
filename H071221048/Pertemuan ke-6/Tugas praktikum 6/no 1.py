a=input("nama file : ")
f=open(f"{a}.txt","w")
f.write('''
Baris pertama
Baris kedua
Dan Seterusnya...''')


b=input("nama file : ")
f=open(f"{b}.txt","a")
fi=open(f"{a}.txt","r")
A=fi.read()
f.write(A)
f.close()
fi.close()

print("Berhasil")
