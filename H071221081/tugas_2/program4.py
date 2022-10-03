times = 0 
newList = []

while times < 3 :
    getNumber = int(input("Masukkan Angka : "))
    newList.append(getNumber)
    times += 1
else:
    biggestNumber = max(newList)
    print("{} adalah angka terbesar".format(biggestNumber))
