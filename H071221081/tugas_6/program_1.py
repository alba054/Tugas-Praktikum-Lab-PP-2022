with open("sample.txt") as f :
    text = f.read()
with open("latihan2.txt",mode="w") as f:
    f.write(text)
with open("latihan2.txt") as f :
    print(f.read())
    