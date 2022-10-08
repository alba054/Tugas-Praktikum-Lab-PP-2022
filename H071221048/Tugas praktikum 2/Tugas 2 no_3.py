a,b,c,d,e=(input()).split()
a= int(a)
b= int(b)
c=int(c)
d=int(d)
e=int(e)
num=a,b,c,d,e
positif = 0
negatif = 0
genap = 0
ganjil = 0
if a > 0:
    positif+=1
elif a<0:
    negatif+=1
if a%2==0:
    genap+=1
elif a%2==1:
    ganjil+=1
if b > 0:
    positif+=1
elif b<0:
    negatif+=1
if b%2==0:
    genap+=1
elif b%2==1:
    ganjil+=1
if c > 0:
    positif+=1
elif c<0:
    negatif+=1
if c%2==0:
    genap+=1
elif c%2==1:
    ganjil+=1
if d > 0:
    positif+=1
elif d<0:
    negatif+=1
if d%2==0:
    genap+=1
elif d%2==1:
    ganjil+=1
if e>0:
    positif+=1
elif e<0:
    negatif+=1
if e%2==0:
    genap+=1
elif e%2==1:
    ganjil+=1
print(f"{positif} angka positif")
print(f"{negatif} angka negatif")
print(f"{genap} angka genap")
print(f"{ganjil} angka ganjil")
# nama = "budi"
# umur = 20

# nama saya budi, umur saya 20
# print("nama saya " + nama + " umur saya " + str(umur))
# print(f"nama saya {nama}, umur saya {umur}")





# print (num)


#bikin file pingpong.py
#n=15
#ping <-- n habis dibagi 3
#pong <-- n habis dibagi 5
# num = "0 1 0 12 2"