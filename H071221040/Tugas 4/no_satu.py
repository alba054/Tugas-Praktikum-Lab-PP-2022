n = int(input('masukkan n:'))

def faktorial(n):
    if n==0 :
        return 1
    else :
        return n*faktorial(n-1)

print(f'faktorial: {faktorial(n)}')

