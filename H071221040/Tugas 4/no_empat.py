def instruksi_robot(x,y):
    count = 1
    while True :
        arah = input('masukkan arah:')
        if count == 1 :
            print (0,0)
        count+=1
        if arah == 'END' :
            break
        else :
            arahan = list(arah)
        for i in arahan :
            if i == 'R' :
                x = x+1
                print(f'{x},{y}')
            elif i == 'L' :
                x = x-1
                print(f'{x},{y}')
            elif i == 'U' :
                y = y+1
                print(f'{x},{y}')
            elif i == 'D' :
                y = y-1
                print(f'{x},{y}')
            else :
                continue

instruksi_robot(0,0)