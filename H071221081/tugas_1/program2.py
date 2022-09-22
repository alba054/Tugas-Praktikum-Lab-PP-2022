inputan = int(input("masukkan akumulasi detik : "))

def method_1(x):
    detik = 0
    menit = 0
    jam = 0
    i = 0   
    while (i+60 < x):
        menit += 1  
        # if i < inputan :
        if menit == 60 :
            jam += 1
            menit = 0 
        i += 60
        detik = x - i
    print("hasil -> {h} : {m} : {s}".format(h= jam,m=menit,s=detik))


def method_2(x):
    detik = (x % 60)
    menit = (x // 60 % 60) 
    jam = (x // 3600) 
    
    print("hasil -> {h} : {m} : {s}".format(h= jam,m=menit,s=detik))
    
method_1(inputan)
method_2(inputan)