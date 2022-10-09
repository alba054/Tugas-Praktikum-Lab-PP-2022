x=int(input("Masukkan harga barang:"))
y=int(input("Masukkan Jumlah uang:"))
z=y-x
while z>0:
    if z>=100000:
        print ("satu uang Rp.10000")
        z-=100000
    elif z>=50000:
        print("satu uang Rp.50000")
        z-=50000
    elif z>=20000:
        print("satu uang Rp.20000")
        z-=20000
    elif z>=10000:
        print(f"satu uang Rp.10000")
        z-=10000
    elif z>5000:
        print("satu uang Rp.5000")
        z-=5000
    elif z>=2000:
        print("satu uang Rp.2000")
        z-=2000
    elif z>=1000:
        print("satu uang Rp.1000")
        z-=1000
if x>y:
    print("Uang tidak cukup")