mat1 = [[int(input(f"Input nilai matriks pertama indeks {a+1 , b+1}:")) for a in range(2)]for b in range(2)]
mat2 = [[int(input(f"Input nilai matriks kedua1 indeks {a+1 , b+1}:")) for a in range(2)]for b in range(2)]

matriks3 = []
a1 = mat1[0][0] * mat2[0][0] + mat1[0][1] * mat2[1][0]
a2 = mat1[0][0] * mat2[0][1] + mat1[0][1] * mat2[1][1]
a3 = mat1[1][0] * mat2[0][0] + mat1[1][1] * mat2[1][0]
a4 = mat1[1][0] * mat2[0][1] + mat1[1][1] * mat2[1][1]
matriks3.append([a1,a2])
matriks3.append([a3,a4])
print("Hasil perkalian matriks")
print(f"{mat1} x {mat2} = {matriks3}")







