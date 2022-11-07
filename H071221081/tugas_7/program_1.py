import re

PATTERN = r"[a-z,A-Z,2,4,6,8]{40}[1,3,5,7,9,\s]{5}"

string = input()
c = re.search(PATTERN,string)
if c : print("true")
else : print("false")