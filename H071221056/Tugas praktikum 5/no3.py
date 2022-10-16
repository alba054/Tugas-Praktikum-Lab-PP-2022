array1 = set(input("input array ke 1: "))
array2 = set(input("input array ke 2: "))
#duplikat = []
#for i in array1:
 #   if array1.count(i)>1:
  #      if i not in duplikat:
   #         duplikat.append(i)

#print(duplikat)

array3 = array1.intersection(array2)
print("terdapat", len(array3), "buah duplikat yaitu", array3)
