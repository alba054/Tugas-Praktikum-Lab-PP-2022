x = int(input('masukkan n: '))
a = 0
b = 1
sum = 0
for i in range(0, x):
    print(sum,end=' ')
    a = b
    b = sum
    sum = a+b


x = ''
for i in range(10) :
    x += str(i) + ' '
    print (x) 
