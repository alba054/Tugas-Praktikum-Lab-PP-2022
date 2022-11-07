import re
a=[]
l=int(input("Masukkan baris : "))
for i in range (l):
    string=input()
    pattern=r"(2?[0-5]?[0-5]?|[0-1]?\d{1,2})\.(2?[0-5]?[0-5]?|[0-1]?\d{1,2})\.(2?[0-5]?[0-5]?|[0-1]?\d{1,2})\.(2?[0-5]?[0-5]?|[0-1]?\d{1,2})$"
    result=re.match(pattern,string)
    if result:
        a.append("IPv4")
    else:
        pattern2=r"([\da-f]{1,4}:){7}([\da-f]{1,4})$"
        result=re.match(pattern2,string)
        if result:
            a.append("IPv6")
        else:
            a.append("Bukan IP adress")
for i in a:
    print(i)
