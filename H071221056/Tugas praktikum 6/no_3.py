x , y = input()+'.txt', int(input())
with open("Tabel.txt", "r") as tabel:
    file_as = tabel.read()
    with open(x, "w") as konten:
        konten.write(file_as)
        for i in range(y):
            a,b,c = input().replace(" ", "_"), input(), input()
            konten.write(f"|{a}{' ' * (31 - len(a))}|{b}{' ' * (14 - len(b))}|{c}{' ' * (12 - len(c))}|\n+-------------------------------+--------------+------------+\n")
            