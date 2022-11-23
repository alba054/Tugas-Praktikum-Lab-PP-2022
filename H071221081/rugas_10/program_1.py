import re

listOfData = []
def detail():
    if len(listOfData) == 0 :
        return "data saat ini kosong"
    else :
        for i in listOfData:
            print("Id           : " + i["id"])
            print("Nama         : " + i["nama"])
            print("Email        : " + i["email"])
            print("password     : " + i["password"])

def ubah():
    if len(listOfData) == 0 :
        return "data saat ini kosong"
    else :
        detail()
        getId = input("masukkan id data ketik 0 untuk keluar : ")
        if getId != "0":
            getNewName = input("masukkan nama baru : ")
            listOfData[int(getId)-1]["nama"] = getNewName
            print("berhasil")
            
def buat():
    counter = len(listOfData) + 1
    data = {
        "id" : str(counter),
        "nama" : "",
        "email" : "",
        "pass" : "",
    }
    emailPatt = r"^[a-z\d]{1,30}@student.unhas.ac.id$"
    passPatt = r"^[a-zA-Z\d]{8,20}$"
    getMail = " "
    getPass = " "
    
    getNama = input("Input Nama         :")
    while not(re.search(emailPatt,getMail)):
        getMail = input("Input Email        :")
        # print(re.search(emailPatt,getMail))
    while not(re.search(passPatt,getPass)):
        getPass = input("Input Password     :")
        
    data["nama"] = getNama
    data["email"] = getMail
    data["password"] = getPass
    
    listOfData.append(data)
    
def jumlah():
    if len(listOfData) == 0 :
        return "data saat ini kosong"
    else :
        numsOfNama = 0
        getFile = input("masukkan Nama File :")
        try:
            with open(getFile + ".txt", "r") as f:
                for i in f:
                    print(i)
                    if "Nama" in i:
                        numsOfNama += 1
                print(numsOfNama)
        except FileNotFoundError:
            return "file tidak ada"

def simpan():
    if len(listOfData) == 0 :
        return "data saat ini kosong"
    else :
        getFile = input("masukkan Nama File :")
        try:
            with open(getFile + ".txt", "w") as f:
                for i in listOfData:
                    f.write("Id       : " + listOfData[i]["id"] + "\n")
                    f.write("Nama       : " + listOfData[i]["nama"] + "\n")
                    f.write("Email      : " + listOfData[i]["email"] + "\n")
                    f.write("password   : " + listOfData[i]["password"] + "\n")
                return "berhasil"
        except FileNotFoundError:
            return "file tidak ada"

if __name__ == '__main__':
    loop = True
    while loop:
        prompts = """
1. Detail Anda
2. Ubah Nama
3. Jumlah Data
4. Save Data
5. Buat Data
6. keluar
        """
        print(prompts)
        getTask = input("masukkan kode tugas : ")
        match (getTask):
            case "1":
                detail()
            case "2":
                ubah()
            case "3":
                jumlah()
            case "4":
                simpan()
            case "5":
                buat()
            case "6":
                exit()
            case default:
                print("masukkan kode yang sesuai")
    # buat()
    # ubah()
    # detail()