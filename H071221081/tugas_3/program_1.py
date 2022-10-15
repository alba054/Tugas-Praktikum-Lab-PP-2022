
try:
    nMax = int(input("masukkan Angka Maksimal : "))
    lMax = int(input("masukkan Panjang Angka : "))

    # print(lMax,nMax)
    for n in range(1,nMax+1):   
        print(n,end=" ")
        if n % lMax == 0:
            print() 
except:
    raise Exception