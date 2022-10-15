get = set(input("masukkan angka : ").split())
get1 = set(input("masukkan angka : ").split())

print(get & get1)

def duplikat(l1,l2):
    l = list(l1)
    l1 = list(l2)
    hasil = []
    for i in l1:
        for j in l:
            if j == i:
                hasil.append(i)
    print(hasil)
    
duplikat(get, get1)