# def faktorial(x):
#     if x == 0:
#         hasil = 0
#         return hasil
#     hasil = 1
#     for i in range(1,x+1):
#         hasil *= i
#     return hasil

def faktorial(x):
    if x == 2:
        return 2
    return faktorial(x-1) * x

# faktorial(4)
# faktorial(3) * 4
# faktorial(2) * 3
    
try:
    get = int(input("masukkan angka untuk difaktorialkan : "))
    print(faktorial(get))

except Exception as e:
    print(e)