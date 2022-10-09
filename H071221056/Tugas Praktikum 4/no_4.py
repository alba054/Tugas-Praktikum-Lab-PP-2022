x = 0
y = 0
while True :
    a =  str(input('String : '))

    if (a == "R") or (a == "r"):
        x = x + 1
        print (x, y)
    elif (a == "L") or (a == "l"):
        x = x - 1
        print (x, y)
    elif (a == "U") or (a == "u"):
        y = y + 1
        print (x, y)
    elif (a == "D") or (a == "d"):
        y = y - 1
        print (x, y)
    elif a == "END":
        break
    
    

    