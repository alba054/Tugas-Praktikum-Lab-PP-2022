def getInput():
    print("Syarat : \nnama tidak boleh lebih dari 20 karakter\n")
    temp = []
    fileName = input("masukkan nama file : ").replace(" ","_")
    numsOfName = int(input("masukkan jumlah inputan : "))
    for i in range(numsOfName):
        asistName = input("Nama Asisten : ")
        asistNIM = input("NIM Asisten : ")
        asistYear = input("Angkatan Asisten : ")
        if len(asistName) > 20 :
            print("gagal")
            exit()
        tempIn = []
        tempIn.append(asistName)
        tempIn.append(asistNIM)
        tempIn.append(asistYear)
        temp.append(tempIn)
    return fileName, temp

def toFile(fileName,datas):
    border = "+{}+{}+{}+\n".format("-"*25,"-"*15,"-"*15)
    dataBorder = "|{: <25}|{: <15}|{: <15}|\n"
    
    with open(f"{fileName}.txt",mode="w") as f : 
        f.write(border)
        f.write(dataBorder.format("Nama","NIM","Angkatan"))
        f.write(border)
        for data in datas:
            f.write(dataBorder.format(data[0],data[1],data[2]))
            f.write(border)
        print("berhasil")

file,data = getInput()
toFile(file,data)
