berat = int(input("Masukkan berat anda = "))
tinggi = int(input("Masukkan tinggi anda = "))

try:
	bmi = berat / (tinggi ** 2)
	print(f"Indeks Massa Tubuh (BMI): {bmi:.2f}")
except ZeroDivisionError: #untuk kesalahan jika memasukkan angka Nol
	print("Error : Tinggi dan Berat tidak boleh Nol")
except Exception as e:
	print("Terjadi kesalahan : ", e)