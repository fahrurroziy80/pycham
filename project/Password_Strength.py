import re

def periksa_password(password):
    panjang = len(password) >= 8
    huruf_besar = bool(re.search(r"[A-Z]", password))
    huruf_kecil = bool(re.search(r"[a-z]", password))
    angka = bool(re.search(r"[0-9]", password))
    simbol = bool(re.search(r"[!@#$%^&*()_+=\[\]{}|\\:;\"'<>,.?/~`-]", password))

    skor = sum([panjang, huruf_besar, huruf_kecil, angka, simbol])

    if skor == 5:
        return "💪 Sangat Kuat"
    elif skor == 4:
        return "👍 Kuat"
    elif skor == 3:
        return "⚠️ Cukup"
    else:
        return "❌ Lemah"

# Masukkan password
password = input("Masukkan password: ")
hasil = periksa_password(password)
print("Kekuatan password kamu:", hasil)
