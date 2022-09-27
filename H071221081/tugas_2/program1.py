nilai = input("Nilai : ")

try:
    nilai = int(nilai)
except :
    print("nilai harus angka")
    quit()

if nilai >= 90:
    grade = "A"
elif nilai >= 80:
    grade = "B"
elif nilai >= 70:
    grade = "C"
elif nilai >= 60:
    grade = "D"
elif nilai >= 50:
    grade = "E"
elif nilai > 40:
    grade = "F"

print("nilai {} : {}".format(nilai,grade))