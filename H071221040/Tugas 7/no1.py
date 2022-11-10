import re
s= input()
if len(s)==45 :
    pola1= r"(\A([A-Z]|[0|2|4|6|8]|[a-z]){40})(\s|1|3|5|7|9)"
    result1= re.match(pola1, s)
    if result1 :
        print("true")
    else :
        print("false")
else :
    print("false")