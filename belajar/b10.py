# --- Belajar Format String dalam Python (Episode 18) ---

# 1. Contoh dasar format string (f-string)
# f-string adalah cara mudah untuk menyisipkan variabel ke dalam string.
print("--- 1. Contoh dasar format string ---")
nama = "Marlin"
format_str = f"Hello {nama}"
print(f"Output: {format_str}\n")

# 2. Format string dengan berbagai tipe data
# f-string bisa langsung memformat dan menampilkan berbagai tipe data.
print("--- 2. Format string dengan berbagai tipe data ---")
angka = 2005.5
format_str_angka = f"Angka = {angka}"
print(f"Output Angka: {format_str_angka}")

boolean = True
format_str_boolean = f"Nilai boolean = {boolean}"
print(f"Output Boolean: {format_str_boolean}\n")

# 3. Menampilkan bilangan bulat (integer)
# Spesifier ':d' digunakan untuk memastikan angka ditampilkan sebagai bilangan bulat.
print("--- 3. Menampilkan bilangan bulat (integer) ---")
angka_bilangan_bulat = 15
format_str_int = f"Ini adalah bilangan bulat = {angka_bilangan_bulat:d}"
print(f"Output: {format_str_int}\n")

# 4. Menampilkan angka ribuan dengan koma (pemisah ribuan)
# Spesifier ':, ' digunakan untuk menambahkan pemisah ribuan (koma).
print("--- 4. Menampilkan angka ribuan dengan koma ---")
angka_jutaan = 2000000
format_str_ribuan = f"Ribuan = {angka_jutaan:,}"
print(f"Output: {format_str_ribuan}\n")

# 5. Menampilkan bilangan desimal dengan presisi tertentu
# Contoh ':.2f' akan memformat angka float menjadi dua angka di belakang koma.
print("--- 5. Menampilkan bilangan desimal dengan presisi tertentu ---")
desimal = 2005.54321
format_str_desimal = f"Desimal (2 angka di belakang koma) = {desimal:.2f}"
print(f"Output: {format_str_desimal}\n")

# 6. Menampilkan Leading Zero (nol di depan)
# Contoh ':010.3f' berarti total 10 karakter (termasuk koma dan desimal),
# dengan 3 angka desimal dan sisanya diisi nol di depan jika kurang dari 10 karakter.
print("--- 6. Menampilkan Leading Zero ---")
angka_dengan_nol = 2005.54321
format_str_leading_zero = f"Leading Zero = {angka_dengan_nol:010.3f}"
print(f"Output: {format_str_leading_zero}\n")

# 7. Menampilkan tanda plus atau minus
# Spesifier ':+d' akan selalu menampilkan tanda (+) untuk angka positif
# dan (-) untuk angka negatif.
print("--- 7. Menampilkan tanda plus atau minus ---")
angka_minus = -10
angka_plus = 10
format_minus = f"Minus = {angka_minus:+d}"
format_plus = f"Plus = {angka_plus:+d}"
print(f"Output Minus: {format_minus}")
print(f"Output Plus: {format_plus}\n")

# 8. Memformat persentase
# Contoh ':.2%' akan mengubah angka desimal menjadi persentase dengan dua angka di belakang koma.
print("--- 8. Memformat persentase ---")
nilai_persen = 0.045
format_persen = f"Persen = {nilai_persen:.2%}"
print(f"Output: {format_persen}\n")

# 9. Melakukan operasi aritmatika di dalam placeholder
# f-string memungkinkan operasi matematika langsung di dalam kurung kurawal {}.
print("--- 9. Melakukan operasi aritmatika dalam placeholder ---")
harga_satuan = 10000
jumlah_barang = 5
format_total = f"Harga total = {harga_satuan * jumlah_barang:,}" # Juga menggunakan pemisah ribuan
print(f"Output: {format_total}\n")

# 10. Format angka ke biner, oktal, dan heksadesimal
# ':b' untuk biner, ':o' untuk oktal, ':x' untuk heksadesimal.
print("--- 10. Format angka ke biner, oktal, dan heksadesimal ---")
angka_konversi = 25
biner_str = f"Biner = {angka_konversi:b}"
oktal_str = f"Oktal = {angka_konversi:o}"
heks_str = f"Hex = {angka_konversi:x}"
print(f"Output Biner: {biner_str}")
print(f"Output Oktal: {oktal_str}")
print(f"Output Hex: {heks_str}\n")