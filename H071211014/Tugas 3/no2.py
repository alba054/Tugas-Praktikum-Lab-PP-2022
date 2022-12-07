for x in range(0,360):
    m = float(input('M(0-360): '))
    if 0 <= m < 90:
        n = m*240
        print('selamat pagi')
        break
    elif 90 <= m < 135:
        n = m*240
        print('selamat siang')
        break
    elif 135 <= m < 180:
        n = m*240
        print('selamat sore')
        break
    elif 180 <= m < 360:
        n = m*240
        print('selamat malam')
        break
    else:
        print('inpput salah')

jam = n // 3600
jam += 6
if jam >= 24:
    jam -= 24
sisa = n % 3600
menit = sisa // 60
detik = sisa % 60

print("%02d:%02d:%02d"%(jam,menit,detik))