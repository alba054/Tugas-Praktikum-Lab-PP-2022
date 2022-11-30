import re

s = input()

if len(s) == 45:
    panjang = r"^[a-zA-Z[02468]{40}[13579\s]{5}"
    kondisi2 = r"[13579\s]"
    kondisi3 = r"[a-zA-Z[02468]"

    pola = re.findall(panjang, s)
    pola1 = re.findall(kondisi2, s[0:40])
    pola2 = re.findall(kondisi3, s[41:45])

    if pola:
        print("True")
    else:
        print("False")

    if pola1 or pola2:
        print(pola1,pola2)

else:
    print("False")