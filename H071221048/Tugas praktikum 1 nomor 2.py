y = int(input("Masukkan angka:"))
SECS_TO_YEAR = (24 * 3600) * 365
tahun = y//SECS_TO_YEAR
SECS_TO_MONTH = (24*3600)*30
z = y%SECS_TO_YEAR
month=z//SECS_TO_MONTH
z= z %SECS_TO_MONTH
hari = z//(3600*24)
z = z%(3600*24)
jam = z // 3600
z = z%3600
menit = z //60
detik = z %60
print(tahun,"tahun",month,"bulan",hari,"hari",jam,"jam",menit,"menit",detik,"detik")