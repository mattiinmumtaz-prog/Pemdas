def hitung_diskon(total):
    if total >= 500000:
        diskon = 0.10 * total
    elif total >= 300000:
        diskon = 0.05 * total
    else:
        diskon = 0
    return diskon

def hitung_total_bayar(total):
    diskon = hitung_diskon(total)
    total_bayar = total - diskon
    return total_bayar

print("MENGHITUNG DISKON BELANJA")

total_belanja = float(input("Masukkan total belanja Anda (Rp): "))

diskon = hitung_diskon(total_belanja)
total_bayar = hitung_total_bayar(total_belanja)

print("Total Belanja : Rp", total_belanja)
print("Diskon        : Rp", diskon)
print("Total Bayar   : Rp", total_bayar)
print("Terimakasih telah berbelanja ^-^")
