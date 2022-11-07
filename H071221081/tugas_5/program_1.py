m1 = [
    [1,2],
    [2,3]]
m2 = [
    [3,4],
    [4,5],
    [1,2]]

m3 = []

try:
    if not(len(m1[0]) == len(m2)):
        raise "salah"
    for i in range(len(m1)):
        baris = []
    for j in range(len(m2[0])):
        hasil = 0
        for k in range(len(m1[0])):
            hasil = hasil + (m1[i][k] * m2[k][j])
        # print(baris)
        baris.append(hasil)
    # print(m3)
    m3.append(baris)
    print(m3)
except :
    print("baris matrix 1 tidak sama dengan kolom matrix 2")

