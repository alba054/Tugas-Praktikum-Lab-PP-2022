a = int(input('Input nilai matriks pertama index 1,1: '))
b = int(input('Input nilai matriks pertama index 1,2: '))
c = int(input('Input nilai matriks pertama index 2,1: '))
d = int(input('Input nilai matriks pertama index 2,2: '))
e = int(input('Input nilai matriks kedua index 1,1: '))
f = int(input('Input nilai matriks kedua index 1,2: '))
g = int(input('Input nilai matriks kedua index 2,1: '))
h = int(input('Input nilai matriks kedua index 2,2: '))

matriks1 = [
    [a, b],
    [c, d],
]

matriks2 = [
    [e, f],
    [g, h],
]

matriks3 = [
    [(a*e)+(b*g), (a*f)+(b*h)],
    [(c*e)+(d*g), (c*f)+(d*h)],
]

for i in range(2):
    if i == 0 :
        print(matriks1[i], 'x', matriks2[i], '=', matriks3[i])
    else :
        print(matriks1[i], ' ', matriks2[i], ' ', matriks3[i])