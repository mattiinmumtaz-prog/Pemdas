menu = 2  

match menu:
    case 1:
        print("Menu 1 belum diisi.")

    case 2:
        i = 1
        while i <= 3:
            print(f"\nPemeriksaan ke-{i}")
            nama = input("Masukkan nama: ")
            sistolik = int(input("Masukkan tekanan darah sistolik (mmHg): "))
            diastolik = int(input("Masukkan tekanan darah diastolik (mmHg): "))
            denyut = int(input("Masukkan denyut nadi (bpm): "))

            print(f"\nHasil untuk {nama}")

            if sistolik > 180 or diastolik > 120:
                print("!!Krisis hipertensi! Segera cari bantuan medis.")
            elif sistolik > 140 or diastolik > 90:
                print("!Tekanan darah tinggi (hipertensi). Konsultasikan ke dokter.")
            elif (120 <= sistolik <= 139) or (80 <= diastolik <= 89):
                print("Prehipertensi. Jaga pola hidup sehat.")
            elif sistolik < 120 and diastolik < 80:
                print("Tekanan darah normal.")
            else:
                print("Data tekanan darah tidak valid atau tidak masuk kategori umum.")

            if denyut > 100:
                print("!!Denyut nadi tinggi (>100 bpm). Periksa kesehatan jantung.")
            elif denyut < 60:
                print("!Denyut nadi rendah (<60 bpm). Waspadai gejala bradikardia.")
            else:
                print("Denyut nadi normal.")

            print("------------------------------")
            i += 1

    case _:
        print("Menu tidak tersedia.")
