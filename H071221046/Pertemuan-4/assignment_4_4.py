#Najwa Hanana
#H071221046
#PERTEMUAN 4


x = 0
y = 0
print (x, y)
while True :
    inp =  str(input('String : '))

    if (inp == "R") :
        x = x + 1
        print (x, y)
    elif (inp == "L") :
        x = x - 1
        print (x, y)
    elif (inp == "U") :
        y = y + 1
        print (x, y)
    elif (inp == "D") :
        y = y - 1
        print (x, y)
    else :
        print ('---')
    
