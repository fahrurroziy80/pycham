from datetime import datetime

def input_tanggal_lahir():
    try:
        # Input dari pengguna
        hari = int(input("Masukkan tanggal lahir (1-31): "))
        bulan = int(input("Masukkan bulan lahir (1-12): "))
        tahun = int(input("Masukkan tahun lahir (cth: 2000): "))

        # Membuat objek tanggal lahir
        tanggal_lahir = datetime(tahun, bulan, hari)
        print(f"Tanggal lahir kamu: {tanggal_lahir.strftime('%d-%m-%Y')}")

        # Tanggal sekarang
        sekarang = datetime.now()

        # Hitung umur
        umur = sekarang.year - tanggal_lahir.year

        if (sekarang.month, sekarang.day) < (tanggal_lahir.month, tanggal_lahir.day):
            umur -= 1

        print(f"Umur kamu sekarang: {umur} tahun")

    except ValueError:
        print("Input tidak valid. Pastikan kamu memasukkan angka dengan benar dan tanggal yang sesuai.")

# Jalankan fungsi
input_tanggal_lahir()
