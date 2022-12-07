file = open('Latihan1.txt','w')
file.write('Baris pertama\n')
file.write('Baris kedua \n')
file.write('Dan Seterusnya... \n')

file.close()

inputan1 = input()
inputan2 = input()

file = open(inputan1 + '.txt','r')
data = file.read()
file.close()

with open(inputan2 + '.txt','w') as file:
    file.write(data)
print('\nBerhasil')