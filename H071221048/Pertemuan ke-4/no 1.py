def factorial(a):
    if a>=0:
        for i in range (1,a):
            a=a*i
        return a
    if a<0:
        print("Faktorial negatif tak terdefinisi")
    
n=(int(input("Masukkan faktorial: ")))

print(f"Faktorial dari {n}! = {factorial(n)}")
    
