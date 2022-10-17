a=[[0,0],
    [0,0]]
b=[[0,0],[0,0]]
a[0][0]=int(input("Input niai matriks pertama index 1,1 : "))
a[0][1]=int(input("Input niai matriks pertama index 1,2 : "))
a[1][0]=int(input("Input niai matriks pertama index 2,1 : "))
a[1][1]=int(input("Input niai matriks pertama index 2,2 : "))

b[0][0]=int(input("Input niai matriks kedua index 1,1 : "))
b[0][1]=int(input("Input niai matriks kedua index 1,2 : "))
b[1][0]=int(input("Input niai matriks kedua index 2,1 : "))
b[1][1]=int(input("Input niai matriks kedua index 2,2 : "))

c=[[0,0],[0,0]]
c[0][0]=a[0][0]*b[0][0]+a[0][1]*b[1][0]
c[0][1]=a[0][0]*b[0][1]+a[0][1]*b[1][1]
c[1][0]=a[1][0]*b[0][0]+a[1][1]*b[1][0]
c[1][1]=a[1][0]*b[0][1]+a[1][1]*b[1][1]
print(f"Hasil perkalian matrix")
print("",a[0],"X",b[0],"\n",a[1]," ",b[1])
print("",c[0],"\n",c[1])