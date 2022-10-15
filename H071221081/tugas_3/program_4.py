
lines = input("masukkan jumlah baris : ")

if not(lines.isnumeric()) :
    raise ValueError

lines = int(lines) + 1
# rule = 2*i-1
for line in range(lines):
    for b in range(lines-1):
        print(" ",end=" ")
    lines -= 1
    for j in range(line*2-1) :
        print("*",end=" ")
    print()