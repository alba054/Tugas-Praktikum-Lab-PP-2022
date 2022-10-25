a = int(input("input nilai matriks pertama index 1,1:"))
b = int(input("input nilai matriks pertama index 1,2 :"))
c = int(input("input nilai matriks pertama index 2,1 :"))
d = int(input("input nilai matriks pertama index 2,2 :"))
e = int(input("input nilai matriks kedua index 1,1 : "))
f = int(input("input nilai matriks kedua index 1,2 :"))
g = int(input("input nilai matriks kedua index 2,1 :"))
h = int(input("input nilai matriks kedua index 2,2 :"))

W = (a * e) + (b * g)
X = (c * e) + (d * g)
Y = (a * f) + (b * h)
z = (c * f) + (d * h)

matriks = []
matriks.append([W,Y])
matriks.append([X,z])

print(f"{[a,b],[c,d]} x {[e,f],[g,h]} ={matriks}")1



