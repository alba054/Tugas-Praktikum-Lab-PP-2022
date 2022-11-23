from math import ceil,sqrt

def prima(x:int) -> bool:
    for i in range(2,x):
        # print(i, x)
        if x % i == 0 :
            return False
    return True 

try:
    get = int(input("masukkan bilangan bulat : "))
    
    if prima(get) :
        print("ini bilangan prima")
    else :
        print("ini bukan bilangan prima")
        
except ValueError:
    print("tipe data yang diinput bukan integer")