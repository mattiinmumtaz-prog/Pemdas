nilai = []

for i in range(5):
    n = int(input(f"Masukkan nilai mahasiswa ke-{i+1}: "))
    nilai.append(n)

print(f"list nilai mahasiswa = {nilai}")

for i in range(5):
    if nilai[i] < 60:
        print(f"Mahasiswa ke-{i+1} Tidak Lulus")
    else:
        print(f"Mahasiswa ke-{i+1} Lulus")

rata = sum(nilai) / len(nilai)
print("Rata-rata nilai mahasiswa:", rata)
