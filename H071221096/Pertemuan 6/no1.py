fileoriginal = input("Masukkan nama file: ")
filecopy = input("Masukkan nama file baru: ")

try:
    with open(f"{fileoriginal}.txt" , 'r') as file:
        a = file.read()    
        
    with open(f"{filecopy}.txt" , 'w') as file:
        file.write(a)
        print("Berhasil")
except:
    print("Gagal")








