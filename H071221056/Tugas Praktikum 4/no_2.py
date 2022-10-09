x = int(input("masukkan bilangan pertama"))
y = int(input("masukkan nilangan kedua"))

def mencari_fpb(a,b):
    bilangan_terkecil = a
    if a > b:
        bilangan_terkecil = b
    elif a < b:
        bilangan_terkecil = a
    else :
        bilangan_terkecil = a or b

    if a==0:
         fpb = b
    elif b==0:
        fpb = a
    for i in range(1, bilangan_terkecil+1):
            if (a % i == 0) and (b % i == 0):
                fpb=i
    return fpb

print(f"FPB dari{x} dan {y} = {mencari_fpb(x,y)}")
