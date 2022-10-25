arr1 = list(input("masukkan array 1 :").split())
arr2 = list(input("masukkan array 2 :").split())

arr3 = []

for i in arr1:
    for j in arr2:
        if i == j:
            arr3.append(j)
print(arr3)
