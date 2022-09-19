import math

height = float(input("masukkan tinggi : "))
angle1 = int(input("masukkan sudut 1 : "))
angle2 = int(input("masukkan sudut 2 : "))

if angle1 < 90 and angle2 < angle1:
    tan1 = math.tan(math.radians(angle1))
    tan2 = math.tan(math.radians(angle2))
    
    floor1 = height * tan1
    floor2 = height * tan2
    
    output = floor1 - floor2
    print("hasil : {:.2f}".format(output))
else:
    print("sudut 2 harus kurang dari sudut 1 dan sudut 1 harus kurang dari 90")
