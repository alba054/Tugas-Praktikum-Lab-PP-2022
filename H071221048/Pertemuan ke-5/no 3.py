a=input("Masukkan array ke-1 : ").split()
#a = set(a)
b=input("Masukkan array ke-2 : ").split()
#b=set(b)
#a.intersection_update(b)
d=[]
for i in a:
    for j in b:
        if i == j:
            d.append(i)
print(f"Terdapat {len(d)} buah duplikat,yaitu {d}")