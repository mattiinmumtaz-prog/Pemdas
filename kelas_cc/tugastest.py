import numpy as np

siswa = np.array ([0,1,2])
nilai = np.array ([[80,75,90,88],[70,60,85,78],[95,88,92,90]])

rata = nilai.mean(axis=0)
nilai_tinggi = nilai.max()
nilai_rendah = nilai.min()
u3 = nilai[0:3,2]
rata_tinggi = rata.max()

print(f"rata-rata nilai siswa adalah = {rata}")
print(f"nilai tertinggi siswa adalah = {nilai_tinggi}")
print(f"nilai terrendah siswa adalah = {nilai_rendah}")
print(f"nilai ujian ke 3 masing-masing siswa = {u3}")
print(f"nilai rata-rata siswa tertinggi adalah = {rata_tinggi}")