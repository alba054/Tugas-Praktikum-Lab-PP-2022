import re

IPV4_PATTERN = r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
# ^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$
IPV6_PATTERN = r"^(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$"

listOfInput = []
getNums = input("masukkan jumlah test : ")
for i in range(1,int(getNums)+1):
    getInput = input(f"case {i} : ")
    listOfInput.append(getInput)
    
for i in listOfInput:
    if re.search(IPV4_PATTERN,i):
        print("IPv4")
    elif re.search(IPV6_PATTERN,i):
        print("IPv6")
    else:
        print("bukan Ip")

