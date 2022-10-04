sample_1 = input("Total Uang : ")
sample_2 = input("Total Pembayaran : ")

# if not(sample_1.isnumeric()) and not(sample_2.isnumeric()):
#     raise ValueError

# sample_1 = int(sample_1)
# sample_2 = int(sample_2)

try:
    sample_1 = int(sample_1)
    sample_2 = int(sample_2)
    calc = sample_1 - sample_2

    money = {"100000" : 0, "50000" : 0, "20000" : 0, "10000" : 0, "5000" : 0, "2000" : 0 , "1000" : 0}

    while calc > 0:
        for k in money.keys():
            # print(k)
            k = int(k)
            if calc - k >= 0:
                # print(k)
                calc = calc - k
                money[str(k)] += 1
                break
            # print(calc)
    else:
        for k,v in money.items():
            print("{} uang Rp {}".format(v,k))
except :
    raise Exception