def faktorial(n):
    if n==0:
        return 1
    else:
        return n*faktorial(n-1)

n = int(input())
print (n, "! =", faktorial(n))

faktorial =  1
a = int(input("masukkan angka"))
for i in range(1,a+1):
    faktorial*=i

print(faktorial)
