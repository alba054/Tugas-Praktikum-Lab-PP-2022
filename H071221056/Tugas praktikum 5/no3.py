array1 = list(map(int,input("input array ke 1: ").split(" ")))
array2 = list(map(int,input("input array ke 2: ").split(" ")))
irisan = []
for i in array2:
   if i in array1: 
      irisan.append(i)
arrays = tuple(irisan)
print(f"terdapat {len(irisan)} duplikat yaitu : {arrays}")