a=input("nama file : ")
f=open(f"{a}.txt","w")
f.write('''
Baris pertama
Baris kedua
Dan Seterusnya...''')
f.close

b=input("nama file : ")
f=open(f"{b}.txt","w")
fi=open(f"{a}.txt","r")
for line in fi:
    f.write(f"{line.rjust(20)}")
f.close()
