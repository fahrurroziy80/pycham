class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

    def perkenalan(self):
        print(f"Halo, saya {self.nama} dengan NIM {self.nim}")

# Membuat object/instance
mhs1 = Mahasiswa("Fahrurrozi", "123456")
mhs2 = Mahasiswa("Dewi", "654321")

# Memanggil method
mhs1.perkenalan()
mhs2.perkenalan()

print("=====================================================")
print("=====================================================")
print("=====================================================")

class ATM:
    def __init__(self, saldo_awal):
        self.saldo = saldo_awal

    def nabung(self, jumlah):
        self.saldo += jumlah
        print(f"Berhasil menabung Rp{jumlah:,}. Saldo sekarang: Rp{self.saldo:,}")

    def tarik_saldo(self, jumlah):
        if jumlah > self.saldo:
            print("Saldo tidak cukup untuk penarikan!")
        else:
            self.saldo -= jumlah
            print(f"Berhasil menarik Rp{jumlah:,}. Saldo sekarang: Rp{self.saldo:,}")

    def cek_saldo(self):
        print(f"Saldo anda saat ini: Rp{self.saldo:,}")

# Membuat object ATM
akun1 = ATM(1000000)

# Simulasi transaksi
akun1.cek_saldo()
akun1.nabung(500000)
akun1.tarik_saldo(300000)
akun1.tarik_saldo(1500000)  # Ini harus gagal karena saldo kurang
akun1.cek_saldo()
