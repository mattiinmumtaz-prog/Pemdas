usia = int(input("Berapa usiamu?"))
n = "Rekomendasi asupan air : \n"

if usia < 18:
	print(n,"Laki-laki = 1,6 liter air \nPerempuan = 1,4 liter")
elif 18 >= usia < 64:
	print(n,"Laki-laki = 2,5 liter air \nPerempuan = 2 liter")
else:
	print(n,"Laki-laki = 2 liter air \nPerempuan = 1,8 liter")