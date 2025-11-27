harga = 25000
penjualan = 10
total = 0

for i in range(1, 6):
	print(f"Penjualan hari ke {i} adalah {penjualan}")
	pendapatan = harga * penjualan
	print (f"Pendapatan setiap hari adalah {pendapatan}")
	penjualan += 2
	total += pendapatan
print(f"Pendapatan total adalah = Rp.{total}")
	