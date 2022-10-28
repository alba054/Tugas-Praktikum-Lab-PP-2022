a=0
b=0
def movement(x,a=0,b=0):
    if x=='END':
        print("Menghentikan program....")
        return x
    else:
        for i in x:
            if i=="D" or i=="U" or i =="R" or i=="L":

                if i=="U":
                    b+=1
                    print(f"x={a}")
                    print(f"y={b}")
                
                elif x == "R"or i=="R":
                    a+=1
                    print(f"x={a}")
                    print(f"y={b}")
                
                elif x == "L" or i=="L":
                    a-=1
                    print(f"x={a}")
                    print(f"y={b}")
               
                
                elif x == "D" or i=="D":
                    b-=1
                    print(f"x={a}")
                    print(f"y={b}")
                
        x=input("String S ")      
        movement(x,a,b)
        
S=input("String S: ")
print(type (S))
movement(S)