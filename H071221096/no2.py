detik_awal = int(input("detik awal : "))

# import math
# jam = math.floor(detik_awal / 3600)
jam = (detik_awal // 3600)
menit = (detik_awal % 3600 // 60)
detik = (detik_awal % 3600 % 60)

print(jam , ":" , menit , ":" , detik )
