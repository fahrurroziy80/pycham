data = [
    ["Nama", "Usia"],
    ["Alice", 30],
    ["Bob", 25],
    ["Charlie", 35]
]


lebar_nama = 15
lebar_usia = 5


print(f"{'Nama':<{lebar_nama}} {'Usia':<{lebar_usia}}")
print("-" * (lebar_nama + lebar_usia + 2))


for row in data[1:]:
    nama, usia = row
    print(f"{nama:<{lebar_nama}} {usia:<{lebar_usia}}")