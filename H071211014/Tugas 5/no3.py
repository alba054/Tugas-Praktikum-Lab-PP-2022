a = list(map(int, input("input array ke 1 : ").split(" ")))
b = list(map(int, input("input array ke 2 : ").split(" ")))

hasil = []

for i in a:
    for j in b:
        if i == j:
            hasil.append(i)

print(f'terdapat {len(hasil)} buah duplikat yaitu {tuple(hasil)}')