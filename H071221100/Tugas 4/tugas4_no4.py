def robot_instruction(x,y) :
    count = 1
    while True :
        direction= input("inser direction :").upper()
        if count == 1 :
            print(f'0,0')
        count+=1
        if direction == "END" :
            break
        else :
            arahan= list(direction)
        for i in arahan :
            if i == 'R' :
                x= x+1
                print(f"{x},{y}")
            elif i == 'L' :
                x= x-1
                print(f"{x}, {y}")
            elif i == 'U' :
                y= y-1
                print(f"{x}, {y}")
            elif i == 'D' :
                y= y+1
                print(f"{x}, {y}")
            else :
                continue
robot_instruction(0,0)
 