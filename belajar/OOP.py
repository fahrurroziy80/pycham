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
