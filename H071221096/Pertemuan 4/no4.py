def robot():
    x = 0 
    y = 0

    while True: 
        gerak = str(input("Gerak robot :"))
        if gerak == 'END':
            break
        else:
            gerakan = gerak
            for i in gerakan:
                if i == 'R':
                    x += 1
                if i == 'L':
                    x -= 1
                if i == 'U':
                    y += 1
                if i == 'D':
                    y -= 1
            
                print(x , y)

robot()

    




