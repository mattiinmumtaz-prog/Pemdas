nama = input("Masukan nama ?")
umur = int(input("Masukan umur ?"))
status = input("Sudah menikah ?")

if umur > 20 and status == "menikah": #setelah kondisi, ketika enter harus tab
	print("Semoga samawa dan segera diberi keturunan")
elif umur <= 20 and status == "menikah": 
	print("Semoga samawa")
else:
	print("Segeralah menikah")
