import random

def teka_teki():

    daftar_teka_teki = [
        {"kata": "python", "petunjuk": "Bahasa pemrograman populer."},
        {"kata": "gajah", "petunjuk": "Hewan darat terbesar."},
        {"kata": "matahari", "petunjuk": "Sumber cahaya di siang hari."},
        {"kata": "air", "petunjuk": "Cairan yang dibutuhkan semua makhluk hidup."},
    ]

    soal = random.choice(daftar_teka_teki)
    jawaban_benar = soal["kata"]
    petunjuk = soal["petunjuk"]

    print("🎮 SELAMAT DATANG DI GAME TEKA-TEKI 🎮")
    print("Petunjuk:", petunjuk)
    print("Jumlah huruf:", len(jawaban_benar))
    print("Kamu punya 3 kali percobaan.\n")

    percobaan = 3
    while percobaan > 0:
        tebak = input("Tebakan kamu: ").lower()

        if tebak == jawaban_benar:
            print("🎉 Benar! Kamu berhasil menebak kata tersebut!\n")
            break
        else:
            percobaan -= 1
            if percobaan > 0:
                print(f"Salah. Coba lagi. Sisa percobaan: {percobaan}\n")
            else:
                print(f"😢 Kamu kalah. Jawaban yang benar adalah: {jawaban_benar}\n")


teka_teki()
