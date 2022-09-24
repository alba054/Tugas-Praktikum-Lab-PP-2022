#konverensi total detik ke waktu
td = int(input("masukan total detik"))
j = td// 3600
s = td % 3600
m = s// 60
d = s % 60
print(j, "jam",m, "menit",d, "detik")