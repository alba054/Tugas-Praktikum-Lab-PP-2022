def soal_2() :
    a = "45"
    b = 50
    a = int(a)
    result = a + b
    print(result)

def soal_3():
    import math
    PI = math.pi
    x = input("diameter lingkaran : ")
    try:
        r = int(x)
        formula = (4/3) * PI * (r ** 3)
        print("hasil ->  {:.2f}".format(formula))
    except :
        print("input bukan angka")
        quit()

soal_3()