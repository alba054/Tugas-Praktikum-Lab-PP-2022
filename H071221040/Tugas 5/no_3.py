array1 = list(map(int, input('Input array ke 1: ').split(' ')))
array2 = list(map(int, input('Input array ke 2: ').split(' ')))
irisan = []

# 2 3 1 4 5
# 2 -- loop 1 --> loop semua array 1 [1 3 1 2 5]
# 3 -- loop 2

for i in array2:
    if i in array1:
        irisan.append(i)
arrays = tuple(irisan)
print(f"Terdapat {len(irisan)} buah duplikat yaitu : {arrays}")