#Case berguna untuk mengecek satu-satu sampai ada yang sama dengan di variable 

hari = input("Masukkan hari = ")

match hari:
	case "Senin":
		print("Hari ini MatKul RPL dan IMK")
	case "Selasa":
		print("Hari ini MatKul PemBasDat")
	case "Rabu":
		print("Hari ini MatKul PemDas dan GFK")
	case "Kamis":
		print("Hari ini MatKul PemWeb")
	case "Jumat":
		print("Hari ini MatKul SO")
	case "Sabtu" | "Minggu":
		print("Libur/Tidak ada MatKul")
	case _:
		print("Masukkan hari yang benar")