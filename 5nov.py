#list
a = [(1,2,3),(2,3,1,4,5)]
b = [1,2,4]

hasil = a[1][1::2]

print(hasil)


#function
def persegi_panjang(p, l):
	luas = p * l
	keliling = 2 * (p+l) 
	return luas, keliling

panjang = int(input("masukkan P ="))
hasil1, hasil2 = persegi_panjang(panjang, 2) 

print(f"luas persegi panjang = {hasil1} dan kelilingnya = {hasil2}")


#multi function
def coba_percabangan (a, b=5):
	if a > b:
		print("Hitungin dong!")
		hasil = a*b
	else:
		print("Tak bisa dihitung")
		hasil = "Gak ada"
	return hasil

def perulangan (a=5):
	i = 3
	while i < a:
		print(f"Angkanya adalah {i}")
		i += 1
	return i

cobain_terus = coba_percabangan(10)
print(f"Hasil Function = {cobain_terus}")
	