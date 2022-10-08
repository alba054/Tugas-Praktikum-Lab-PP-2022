try:
    degree = float(input("masukkan derajat : "))
    fullTime = (degree * 3600) / 15 

    hour = int(fullTime / 3600 % 24 + 6)
    second = int(fullTime % 60)
    minute = int(fullTime // 60 % 60)  

    if hour < 6:
        print("Selamat Pagi")
    if hour >= 6 and hour < 12:
        print("Selamat Siang")
    if hour >= 12 and hour < 18:
        print("Selamat Sore")
    if hour >= 18:
        print("Selamat Malam")
    print("{:02d}:{:02d}:{:02d}".format(hour,minute,second)) 
except: 
    raise Exception