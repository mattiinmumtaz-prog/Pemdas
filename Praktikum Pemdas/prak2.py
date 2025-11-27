#rata nilai, nilai rata tertinggi, dan rata nilai kelas
siswa = [
    ["Alice", [85, 90, 88]],
    ["Bob", [78, 82, 85]],
    ["Charlie", [92, 88, 90]]
]

for nama, nilai in siswa:
    rata = sum(nilai) / len(nilai)
    print("Rata-rata", nama, "adalah", round(rata, 2))

tertinggi_nama = ""
tertinggi_nilai = 0

for nama, nilai in siswa:
    rata = sum(nilai) / len(nilai)
    if rata > tertinggi_nilai:
        tertinggi_nilai = rata
        tertinggi_nama = nama

print("Siswa dengan nilai tertinggi:", tertinggi_nama, "(", round(tertinggi_nilai, 2), ")")

semua_nilai = []

for nama, nilai in siswa:
    for n in nilai:
        semua_nilai.append(n)

rata_kelas = sum(semua_nilai) / len(semua_nilai)
print("Nilai rata-rata kelas:", round(rata_kelas, 2))
