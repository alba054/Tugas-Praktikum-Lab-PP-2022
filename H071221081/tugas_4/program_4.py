# def convert(x):
#     listx = []
#     listx[:0] = x
#     return listx

def combine(getx):
    newList = []
    # toList = convert(get)
    # temp = ""

    # for i in range(len(get)):
    #     temp = toList[0]
    #     del toList[0]
    #     toList.append(temp)
    #     hasil = "".join(toList)
    #     newList.append(hasil)
    
    for i in range(len(getx)):
        temp = getx[i:] + getx[:i]
        newList.append(temp)
        
    return newList
    
get = input("masukkan kata : ")
hasil = print(combine(get))
