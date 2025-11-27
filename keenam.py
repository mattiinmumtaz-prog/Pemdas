#Jika ditanya gender dan simple
usia = int(input("Berapa usiamu?"))
gender = input("Apa gendermu? (laki-laki/perempuan)")
n = "Rekomendasi asupan air"

if usia < 2:	
	if gender =="laki-laki":
		print("Masih diberi Asi")
	else:
		print("Masih diberi Asi")
elif 2 >= usia < 18:
	if gender == "laki-laki":
		print(n,"= 1,6 Liter air")
	else:
		print(n,"= 1,4 Liter air")
elif 18 >= usia < 64:
	if gender == "laki-laki":
		print(n,"= 2,5 Liter air")
	else:
		print(n,"= 2 Liter air")
elif usia >= 64:
	if gender == "laki-laki":
		print(n,"= 2 Liter air")
	else:
		print(n,"= 1,8 Liter air")
