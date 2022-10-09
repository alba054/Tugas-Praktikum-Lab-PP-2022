n=int(input("Masukkan suku:"))
r=[]
if n < 0:
  print("input harus positif")
elif  n==1:
  r=[0]
else:
  r=[0,1]
  for i in range(2,n):
    r.append(r[i-1]+r[i-2])
print (r)
