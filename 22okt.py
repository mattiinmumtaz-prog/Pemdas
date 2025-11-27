i = 0
while i < 5:
    username = input("Masukan USN anda : ")
    password = int(input("Masukkan sandi anda : "))

    # harus keduanya benar -> maka login berhasil
    if username == "itenas" and password == 123:
        print("Anda berhasil login")
        break
    else:
        print("Anda gagal login")
        i += 1

        # jika sudah percobaan ke-3 (i menjadi 4) => blokir / berhenti
        if i == 4:
            print("Tidak bisa login, tunggu beberapa saat")
            break
