#Najwa Hanana
#H071221046

array1 = set(map(int, input("Input array ke 1 : ").split()))
array2 = set(map(int, input("Input array ke 2 : ").split()))

hasil = array1.intersection(array2)
hasil = tuple(hasil)

print (f'Terdapat {len(hasil)} buah duplikat yaitu {hasil}')