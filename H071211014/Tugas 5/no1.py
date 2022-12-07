def matriks(x,y):
    data =[]
    for i in range(x):
        kal =[]
        for j in range(y):
            isi = int(input("Input nilai matriks index {},{}: ".format(i+1,j+1)))
            kal.append(isi)
        data.append(kal)
    return data

def perkalian_matriks(a,b):
    hasil = []
    for y in range (2):
        total = []
        for x in range (2):
            kali = a[y][0] * b[0][x] + a[y][1] *b[1][x]
            total.append(kali)
        hasil.append(total)
    return hasil

matriks_1 = matriks(2,2)
matriks_2 = matriks(2,2)
kali = perkalian_matriks(matriks_1,matriks_2)

print(f'|{matriks_1[0]}| x |{matriks_2[0]}| = |{kali[0]}|')
print(f'|{matriks_1[1]}|   |{matriks_2[1]}|   |{kali[1]}|')