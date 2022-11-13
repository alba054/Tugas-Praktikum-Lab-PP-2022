import re

user = input('Input : ')

if re.match(r'[a-zA-Z02468]', user[:40]):
    if re.match(r'[13579\s]', user[-5:]):
        print("True")
    else:
        print("False")
else:
    print("False")