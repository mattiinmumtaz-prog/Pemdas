List_satu = [1,1,2,3,4,5,6,7,6,6,6,6]

List_satu[1] = 100
#[1,100,2,3,4,5,6,7,6,6,6,6]

List_satu.insert(2, 120)
#[1,100,120,2,3,4,5,6,7,6,6,6,6]

List_satu.append(190)
#[1,100,120,2,3,4,5,6,7,6,6,6,6,190]

List_satu.pop(0)
#[100,120,2,3,4,5,6,7,6,6,6,6,190]

List_satu.remove(6)
#[100,120,2,3,4,5,7,6,6,6,190]

a = len(List_satu)   # 12
b = sum(List_satu)   # 4xx

print(f"data pada list adalah {List_satu}, panjang List adalah {a}, jumlah total isi didalam list adalah {b}")
