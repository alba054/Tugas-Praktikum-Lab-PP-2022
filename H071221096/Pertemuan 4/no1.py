x = int(input("Masukkan nilai : "))

def faktorial(n):   
    hitung =  1
    for i in range(n, 1, -1):
        hitung = hitung * i

    print(hitung)

faktorial(x)