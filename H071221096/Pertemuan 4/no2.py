a = int(input("Masukkan nilai x : "))
b = int(input("Masukkan nilai y : "))

def getFPB(x , y):
    bilangan_terkecil = 0
    if x > y:
        bilangan_terkecil = y
        print(bilangan_terkecil)

    else:
        bilangan_terkecil = x

    if x == 0:
        fpb = y
    elif y == 0:
        fpb = x 
    else:
        fpb = 0

        for i in range (1, bilangan_terkecil + 1):
            if (x % i == 0) and (y % i == 0):
                fpb = i

    return fpb

print("FPB dari" , a , "dan" , b , "=" , getFPB(a , b)) 

