# Membuat kamus
data = {"nama": "Alice",
        "usia": 30,
        "kota": "New York"}

# Mengakses nilai berdasarkan kunci
print(data["nama"])  # Output: Alice

# Menambahkan pasangan kunci-nilai baru
data["profesi"] = "Insinyur"
print(data["profesi"])

# Mengubah nilai yang sudah ada
data["usia"] = 31

# Menghapus pasangan kunci-nilai
del data["kota"]

print("========================")
# Mengecek apakah kunci ada
if "nama" in data:
    print("Kunci 'nama' ada")
else:
    print("tidak ada kunci ")
if "profesi" in data :
    print("profersi ada di dalam kamus ")
