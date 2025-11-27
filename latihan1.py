total = 0
for i in range(5):
	nilai = float(input(f"Masukkan Nilai Mahasiswa (0-100) ke{i} = "))
	total += nilai
	print (total)
	rata = total / 5
 
if rata >= 60:
	print("Lulus")
else:
	print("Tidak Lulus")