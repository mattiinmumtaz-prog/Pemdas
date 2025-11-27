nilai_murid = {
    'murid1': {
        'nama': 'Alice',
        'usia': 20,
        'nilai': {
            'matematika': 88,
            'sains': 92,
            'bahasa_inggris': 85
        }
    },
    'murid2': {
        'nama': 'Bob',
        'usia': 22,
        'nilai': {
            'matematika': 78,
            'sains': 85,
            'bahasa_inggris': 80
        }
    },
    'murid3': {
        'nama': 'Charlie',
        'usia': 21,
        'nilai': {
            'matematika': 95,
            'sains': 90,
            'bahasa_inggris': 92
        }
    }
}

# print semua murid
for murid in nilai_murid:
    print(murid)

# print hanya nilai matematika dari murid 2
print(nilai_murid['murid2']['nilai']['matematika'])

#print nama murid 3
print(nilai_murid['murid3']['nama'])

#buat percabangan jika matematika dibawah 80 atau nilai bahasa_inggris dibawah 80 maka murid bersangkutan harus belajar lagi, jika tidak maka siswa tersebut aman

print("\nHasil evaluasi belajar:")
for murid, data in nilai_murid.items():
    nama = data['nama']
    nilai_math = data['nilai']['matematika']
    nilai_bing = data['nilai']['bahasa_inggris']

    if nilai_math < 80 or nilai_bing < 80:
        print(f"{nama} harus belajar lagi.")
    else:
        print(f"{nama} aman.")
