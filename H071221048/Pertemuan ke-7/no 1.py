
import re
stirng=input()
pattern= r"^[a-zA-Z24680]{40}[13579\s]{5}$"
result=re.findall(pattern,stirng)
if result:
    print(True)
else:
    print(False)