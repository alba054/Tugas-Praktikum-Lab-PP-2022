x=0
y=0
def kanan():
    global x
    x = x+1
    print(f"x{x}, y{y}")
def kiri():
    global x
    if x!=0:
        x= x-1
    print(f"x{x}, y{y}")
def atas():
    global y
    if(y>0):
        y= y-1
    print(f"x{x}, y{y}")
def bawah():
    global y
    y= y+1
    print(f"x{x}, y{y}")

while True :
    direction= input("inser direction :").upper()
    if direction == "END" :
        break
    else :
        arahan= list(direction)
    for i in arahan :
        if i == 'R' :
            kanan()
        elif i == 'L' :
            kiri()
        elif i == 'U' :
            atas()
        elif i == 'D' :
            bawah()
        else :
            continue