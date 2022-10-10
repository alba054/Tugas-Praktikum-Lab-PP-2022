n = int(input('jumlah baris dan kolom : '))
list = [[int(input(f'masukkan baris {i} dan kolom {j} :')) for i in range(1,n+1)] for j in range(1,n+1)]

diagonal_1 = []
for i in range (0,n):
    for j in range (0,n):
            penjumlahan = list[i][j]
            diagonal_1.append(penjumlahan)

list.reverse()
diagonal_2 = []
for k in range(0,n):
    penjumlahan = list[k][k]
    diagonal_2.append(penjumlahan)

print (f'selisih diagonal = {(sum(l for l in diagonal_2))-(sum(l for l in diagonal_1))}')