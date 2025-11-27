#Jika ditanya gender
usia = int(input("Berapa usiamu?"))
gender = input("Apa gendermu? (laki-laki/perempuan)")
n = "Rekomendasi asupan air"

if usia < 18 and gender == "laki-laki":
	print(n,"= 1,6 Liter air")
elif usia < 18 and gender == "perempuan":
	print(n,"= 1,4 Liter air")
elif 18 >= usia < 64 and gender == "laki-laki":
	print(n,"= 2,5 Liter air")
elif 18 >= usia < 64 and gender == "perempuan":
	print(n,"= 2 Liter air")
elif usia >= 64 and gender == "laki-laki":
	print(n,"= 2 Liter air")
else:
	print(n,"= 1,8 Liter air")