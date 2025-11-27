# =========================
# DATABASE AKUN DUMMY
# =========================
akun_dummy = [("admin", "1234"), ("user1", "pass1"), ("user2", "pass2")]

# =========================
# LOGIN MAKSIMAL 3 KALI
# =========================
percobaan = 0
login_sukses = False

while percobaan < 3:
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    if (username, password) in akun_dummy:
        print("Login berhasil!")
        login_sukses = True
        break
    else:
        percobaan += 1
        print(f"Login gagal! Percobaan ke-{percobaan}/3")

if not login_sukses:
    print("Akun diblokir!")
    exit()

# =========================
# DATA DASAR
# =========================
produksi = {"anak-anak": 0.3, "remaja": 0.5, "dewasa": 0.8, "lansia": 0.6}
jenis_sampah = {"organik": 0.5, "anorganik": 0.3, "b3": 0.05, "lainnya": 0.15}
daur_ulang = {"tidak": 0, "rendah": -0.10, "sedang": -0.20, "tinggi": -0.35}

# =========================
# INPUT JUMLAH RUMAH
# =========================
while True:
    try:
        total_rumah = int(input("\nMasukkan jumlah rumah yang akan diproses: "))
        if total_rumah > 0:
            break
        else:
            print("Angka harus > 0")
    except:
        print("Masukkan angka valid!")

rumah_ke = 1
total_akumulasi = 0  # total gabungan semua rumah

# =========================
# LOOP PER RUMAH TANGGA
# =========================
while rumah_ke <= total_rumah:
    print(f"\n--- Rumah ke-{rumah_ke} ---")
    nama = input("Nama kepala rumah tangga: ")

    # Jumlah anggota
    while True:
        try:
            anggota = int(input("Jumlah anggota: "))
            if anggota > 0:
                break
            else:
                print("Angka harus > 0")
        except:
            print("Masukkan angka valid!")

    # Usia dominan
    while True:
        usia = input("Usia dominan (anak-anak/remaja/dewasa/lansia): ").lower()
        if usia in produksi:
            break
        else:
            print("Kategori salah, masukkan lagi")

    # Jenis sampah
    while True:
        jenis = input("Jenis sampah utama (organik/anorganik/b3/lainnya/campuran): ").lower()
        if jenis in ["organik", "anorganik", "b3", "lainnya", "campuran"]:
            break
        else:
            print("Kategori salah, masukkan lagi")

    # Daur ulang
    while True:
        daur = input("Kebiasaan daur ulang (tidak/rendah/sedang/tinggi): ").lower()
        if daur in daur_ulang:
            break
        else:
            print("Kategori salah, masukkan lagi")

    # =========================
    # PERHITUNGAN SAMPAH
    # =========================
    total = anggota * produksi[usia]
    total_setelah = total * (1 + daur_ulang[daur])
    total_akumulasi += total_setelah

    # Rincian jenis sampah
    if jenis == "campuran":
        rincian = {k: total_setelah * v for k, v in jenis_sampah.items()}
    else:
        rincian = {k: (total_setelah if k == jenis else 0) for k in jenis_sampah}

    # =========================
    # OUTPUT PER RUMAH
    # =========================
    print(f"\n--- Hasil Rumah {nama} ---")
    print(f"Total sampah sebelum pengurangan: {total:.2f} kg")
    print(f"Total sampah sesudah pengurangan: {total_setelah:.2f} kg")
    print("Rincian jenis sampah (kg):")
    for k, v in rincian.items():
        print(f"  {k.capitalize()}: {v:.2f}")

    # Saran singkat
    if rincian["organik"] > max(rincian.values()):
        print("Saran: Prioritaskan kompos!")

    rumah_ke += 1

# =========================
# REKAP TOTAL SEMUA RUMAH
# =========================
print("\n=== Rekap Total Semua Rumah ===")
print(f"Total gabungan sampah sesudah pengurangan: {total_akumulasi:.2f} kg")
