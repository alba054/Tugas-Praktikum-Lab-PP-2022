# def faktorial(x):
#     if x == 0:
#         hasil = 0
#         return hasil
#     hasil = 1
#     for i in range(1,x+1):
#         hasil *= i
#     return hasil

def faktorial(x):
    hasil = x * x-1
    return faktorial(-1)
    
try:
    get = int(input("masukkan angka untuk difaktorialkan : "))
    print(faktorial(get))

except Exception as e:
    print(e)