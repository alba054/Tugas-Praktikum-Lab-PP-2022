with open("sample.txt") as f :
    text = f.read().split()
with open("latihan3.txt",mode="w") as f:
    for line in text:
        f.write("{: >20} \n".format(line))
with open("latihan3.txt") as f :
    print(f.read())
    