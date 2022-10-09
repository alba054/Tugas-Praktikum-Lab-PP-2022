import textwrap
x=int(input("Masukkan X:"))
y=int(input("Masukkan Y:"))
a=[]
for i in range(1,y+1):
   a.append(i)
b=0
c=0
z=x
while b<y/z:
   print(a[c:x])
   b+=1
   c+=z
   x+=z
   


