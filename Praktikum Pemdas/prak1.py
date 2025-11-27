#operator aritmatika dan input

panjang = int(input("Masukkan Panjang Balok = "))
lebar = int(input("Masukkan Lebar Balok = "))
tinggi = int(input("Masukkan Tinggi Balok = "))

print("Panjang = ", panjang)
print("Lebar = ", lebar)
print("Tinggi = ", tinggi)

volume = panjang * lebar * tinggi
print("Volume Balok = ", volume)

#operator perbandingan dan kondisional
nilai = int(input("Masukkan nilai = "))

if nilai >= 70:
	print("LULUS")
elif 50 <= nilai <=69:
	print("REMEDIAL")
else:
	print("GAGAL")

#for loop dan while loop
nama = input("Masukkan nama = ")

for i in range(5):
	print(nama)
i = 0
while i < 5:
	print(nama)
	i += 1