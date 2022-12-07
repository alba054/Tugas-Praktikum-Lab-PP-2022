n = int(input())

def faktorial (n):
  if n > 2:
    return n*faktorial(n - 1)
  return 2

hitung_faktorial = faktorial(n)
print(f'{hitung_faktorial}')