print("### Program Rekomendasi Asupan Air Harian ###")

try:
    nama = input("Masukkan nama: ")
    usia = int(input("Masukkan usia : "))
    jenis_kelamin = input("Masukkan jenis kelamin (laki-laki/perempuan): ").lower()
    aktivitas = input("Masukkan tingkat aktivitas (sedentari/ringan/sedang/berat/atlet): ").lower()
    kondisi = input("Masukkan kondisi kesehatan (tidak ada/hamil/menyusui/demam/ginjal/jantung): ").lower()

    if usia < 3:
        print(f"\n{nama}, usia {usia} tahun: masih diberi ASI, belum perlu perhitungan air harian.")
        exit()
    elif 3 <= usia <= 18:
        if jenis_kelamin == "laki-laki":
            rekom_dasar = 1.6
        elif jenis_kelamin == "perempuan":
            rekom_dasar = 1.4
        else:
            raise ValueError("Jenis kelamin tidak valid.")
    elif 18 < usia <= 64:
        if jenis_kelamin == "laki-laki":
            rekom_dasar = 2.5
        elif jenis_kelamin == "perempuan":
            rekom_dasar = 2.0
        else:
            raise ValueError("Jenis kelamin tidak valid.")
    elif usia >= 65:
        if jenis_kelamin == "laki-laki":
            rekom_dasar = 2.0
        elif jenis_kelamin == "perempuan":
            rekom_dasar = 1.8
        else:
            raise ValueError("Jenis kelamin tidak valid.")
    else:
        raise ValueError("Usia tidak valid.")

    # Faktor aktivitas
    if aktivitas == "sedentari":
        tambahan_aktivitas = 0
    elif aktivitas == "ringan":
        tambahan_aktivitas = 0.3
    elif aktivitas == "sedang":
        tambahan_aktivitas = 0.5
    elif aktivitas == "berat":
        tambahan_aktivitas = 0.8
    elif aktivitas == "atlet":
        tambahan_aktivitas = 1.0
    else:
        raise ValueError("Tingkat aktivitas tidak valid.")

    if kondisi == "tidak ada":
        tambahan_kondisi = 0
    elif kondisi in ["hamil", "menyusui"]:
        tambahan_kondisi = 0.5
    elif kondisi in ["demam", "infeksi"]:
        tambahan_kondisi = 0.7
    elif kondisi == "ginjal":
        tambahan_kondisi = -0.3
    elif kondisi == "jantung":
        tambahan_kondisi = -0.2
    else:
        raise ValueError("Kondisi kesehatan tidak valid.")

    total = rekom_dasar + tambahan_aktivitas + tambahan_kondisi

    # Tampilkan hasil
    print("\n!!! HASIL REKOMENDASI !!!")
    print(f"Nama: {nama}")
    print(f"Usia: {usia} tahun")
    print(f"Jenis kelamin: {jenis_kelamin.capitalize()}")
    print(f"Aktivitas: {aktivitas.capitalize()}")
    print(f"Kondisi kesehatan: {kondisi.capitalize()}")
    print(f"Rekomendasi asupan air harian: {total:.1f} liter per hari")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Terjadi kesalahan: {e}")
