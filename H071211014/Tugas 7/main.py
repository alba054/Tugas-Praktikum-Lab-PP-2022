import re
s = input()

if len(s) == 45:
    syarat_full = r"^[a-zA-Z[02468]{40}[13579\s]{5}"
    syarat2 = "[13579\s]"
    syarat3 = "[a-zA-Z[02468]"

    pola_full = re.findall(syarat_full, s)
    pola1 = re.findall(syarat2, s[0:40])
    pola2 = re.findall(syarat3, s[41:45])

    if pola_full:
        print("True")
    else:
        print("False")

    if pola1 or pola2:
        print(pola1,pola2)

else:
    print("False")

n = input()
ipv4 = input()
ipv6 = input()

if (re.search(n)):
    print("Bukan IP addres")
    if (re.search(ipv4)):
        patter =  "^(25[0-5]| 2[0-4][0-9]|1[0-9]|[0-9][1-9]?[0-9]\.) $",re.split(".")
        print("IPv4")
    else:
        print("Bukan IP address")
    if (re.search(ipv6)):
        pattern = "[0-9]{4}re.split(:)\.[a-z]{0,32}"
        print("IPv6")
    else:
        print("Bukan IP address")