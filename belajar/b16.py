import re
from ssl import create_default_context

#contoh
teks = "Saya belajar python di tahun 22222"

#mencari angka 4 digit
pattern = r"\d{5}"

hasil = re.search(pattern, teks)
if hasil:
    print(f"ketemu: {hasil.group()}")
else:
    print("angka tidak di temukan  ")



print("======================")
print("Mencari Email")
print("======================")

text = "kontak saya di Fahrurrozi@gmail.com"
pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"

email = re.search(pattern, text)

if email:
    print(f"Email ditemukan: {email.group()}")


print("===========================")
print("Validasi Nomor hp")
print("===========================")

teks = "HP saya 081234567890"
pattern = r"08\d{8,11}"

nomor_hp = re.search(pattern, teks)
if nomor_hp:
    print(f"Nomor HP valid: {nomor_hp.group()}")



print("==================")
print("Mengganti Teks ")
print("==================")

teks = "saya pakai bahasa pemrogramman golang"
pattern = r"golang"

teks_baru = re.sub(pattern, "python", teks)
print(teks_baru)


print("===============================================================")

teks = "No NIK  saya 0812345678901212"
pattern = r"08\d{8,16}"

nomor_hp = re.search(pattern, teks)
if nomor_hp:
    print(f"No NIK : {nomor_hp.group()}")

print("==================================================================")
