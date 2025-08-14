# new_list = [ekspresi for item in iterable]
#contoh "Ambil x dari angka, kalau x > 2 simpan x**2 ke list baru."
angka = [1,2,3,4,5]
kuadrat = [x**2 for x in angka]
print(kuadrat)

print("=======================")
print("dengan kondisi (if)")
print("=======================")
#[ekspresi for item in iterabel if kodisi]
angka = [1,2,3,4,5,6]
genap = [x for x in angka if x % 2 == 0]
print("hasil",genap)

print("=======================")
print("dengan if else")
print("=======================")
#[hasil_if_true if kodisi else hasil_if_fale for item in iterable]
angka = [1,2,3,4,5]
label = ["genap " if x % 2 == 0 else "ganjil " for x in angka]
print("hasil", label)

print("==================================")
print("Nested loop (loop dalam loop)")
print("==================================")
#[ekspresi for item1 in iterable1 for item2 in iterable2]
warna = ["merah", "hitam"]
bentuk = ["lingkaran", "kotak"]
kombinasi = [f"{w} {b}" for w in  warna for b in bentuk]
print("hasil :", kombinasi)

print("======================================================")
print("dari string ke int")
print("======================================================")
huruf = [char for char in "fahrurrozi"]
print(huruf)

print("========================================================")
print("dari liost of list (flatten list)")
print("========================================================")
nested = [[1,2], [3,4],[5,6]]
flat = [num for sublist in nested for num in sublist]
print(flat)






























