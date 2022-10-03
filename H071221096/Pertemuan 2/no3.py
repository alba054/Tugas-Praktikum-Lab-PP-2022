try :   
    a = int(input("a : "))
    b = int(input("b : "))
    c = int(input("c : "))
    d = int(input("d : "))
    e = int(input("e : "))

    genap = 0
    ganjil = 0
    positif = 0
    negatif = 0
    nol = 0

    if a % 2 == 0 :
        genap += 1 
    else:
        ganjil += 1
    if a == 0:
        nol += 1
    elif a>0:
        positif += 1
    else:
        negatif += 1

    if b % 2 == 0 :
        genap += 1 
    else:
        ganjil += 1
    if b == 0:
        nol += 1
    elif b>0:
        positif += 1
    else:
        negatif += 1

    if c % 2 == 0 :
        genap += 1 
    else:
        ganjil += 1
    if c == 0:
        nol += 1
    elif c>0:
        positif += 1
    else:
        negatif += 1

    if d % 2 == 0 :
        genap += 1 
    else:
        ganjil += 1
    if d == 0:
        nol += 1
    elif d>0:
        positif += 1
    else:
        negatif += 1

    if e % 2 == 0 :
        genap += 1 
    else:
        ganjil += 1
    if e == 0:
        nol += 1
    elif e>0:
        positif += 1
    else:
        negatif += 1
    
    print (genap , "Angka Genap") 
    print (ganjil , "Angka Ganjil")
    print (positif , "Angka Positif")
    print (negatif , "Angka Negatif")
    print( nol, "Angka nol")
    
except :
    print("Inputan tidak valid")


