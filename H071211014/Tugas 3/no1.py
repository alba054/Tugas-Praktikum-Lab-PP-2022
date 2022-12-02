x = int(input('masukkan nilai x :'))
y = int(input('masukkan nilai y :'))

for i in range(1,y+1) :
    print (i, end="" )
    if i % x == 0 :
        print ()