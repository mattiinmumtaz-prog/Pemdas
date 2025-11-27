#Quiz Toko Roti "Manis Pagi"

harga = 8000
penjualan = 30
total = 0

for i in range (1, 7):
	print(f"Penjualan hari ke {i} sebanyak {penjualan} roti")
	pendapatan = harga * penjualan
	print (f"Pendapatan hari {i} adalah Rp.{pendapatan}")
	penjualan += 4
	total += pendapatan
print(f"Pendapatan total selama {i} hari adalah : Rp.{total}")
	