def fpb(x,y):
    if x <= y:
        min = x
    elif y <= x:
        min = y
    for i in range(1,min+1):
        if x % i == 0 and y % i == 0:
            fpb = i
    return fpb

num1 = int(input("masukkan angka : "))
num2 = int(input("masukkan angka : "))
fpb = fpb(num1,num2)
print(fpb)