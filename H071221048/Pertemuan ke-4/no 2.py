def Hitung_FPB(x,y):
    for i in range (1,y+1):
        if x%i==0 and y%i==0:
            FPB=i
    return FPB 
x=int(input("Masukkan x: "))
y=int(input("Masukkan y: "))
print(Hitung_FPB(x,y))