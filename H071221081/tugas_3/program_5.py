sample_1 = input("panjang fibonacci : ")

# if not(sample_1.isnumeric()):
#     raise ValueError

# sample_1 = int(sample_1)

try:
    
    sample_1 = int(sample_1)
    newList = [0,1]
    
    while len(newList) <= sample_1:
        newItem = newList[-2] + newList[-1]
        newList.append(newItem)
    else:
        print(newList[:sample_1])
    # newList[:sample_1]
except :
    raise Exception