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

teks1 = 'Baris pertama'
teks2 = 'Baris kedua \n'
teks3 = 'Dan Seterusnya... '
data1 = '\n{:>15}'.format(teks1)
data2 = '\n{:>20}'.format(teks2)
with open(inputan2 + '.txt','a') as file:
    file.write(data1)
    file.write(data2)
    file.write(teks3)
print('\nBerhasil')