def customSort(listx,reverse=False):
    for c in range(len(listx)):
        print(c)
        for n in range(c+1,len(listx)):
            print(n)
            if listx[c] > listx[n] :
                temp = listx[c]
                listx[c] = listx[n]
                listx[n] = temp
    
    if reverse == True:
        return listx[::-1]
    return listx

# get = input("masukkan angka : ")
# listx = get.split(get)
# print(customSort(listx,reverse=True))
print(customSort([7,4,2,1,3,2],reverse=True))