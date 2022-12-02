#Merubahdetik ke jam menit dan detik

#deklarasi
class Waktu: 
    jj = 0 
    mm = 0
    dd = 0
    
jam = Waktu()
TotalDetik = 0

#Algoritma
j = input("masukkan jam:")
m = input("masukkan menit:")
d = input("masukkan detik:")

jam.jj = int(j)
jam.mm = int(m)
jam.dd = int(d)
print("jam: ",jam.jj,":",jam.dd)