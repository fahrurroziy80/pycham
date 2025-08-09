


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


print("==============================================================")
print("Methods and Dunder")
print("===============================================================")
class Mobil:
    def __init__(self, merek, warna):
        self.merek = merek
        self.warna = warna

    def info(self):
        return f"Mobil {self.merek} berwarna {self.warna}"

    def nyalakan(self):
        return "Mesin sudah menyala dan siap berangkat "

#membuat objek
lamborgini = Mobil("Lamborgini", "Hitam")

#Memanggil method
print(lamborgini.info()) #mobil lambo berwarna hitam
print(lamborgini.nyalakan()) # mesin manyala

print("===============================================================")
print("jenis Methods and Dunder")
print("===============================================================")
#__init__ (Constructor)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Budi", 20)
print(p.name)  # Budi
print("===============================")
#__str__ (Representasi string untuk user)
class Person:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"Nama: {self.name}"

p = Person("Andi")
print(p)  # Nama: Andi

print("===============================")
# __repr__ → Representasi string untuk developer
class Person:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f"Person(name={self.name!r})"

p = Person("Dewi")
print(repr(p))  # Person(name='Dewi')

print("===================================")
#__len__ penjang objek
class Team:
    def __init__(self, member):
        self.member = member
    def __len__(self):
        return len(self.member)
t = Team(["A", "B", "C"])
print(len(t))

print("==========================================")
#__getitem__ & __setitem__ → Akses seperti list/dict
class MyList:
    def __init__(self):
        self.data = []
    def __getitem__(self, index):
        return self.data[index]
    def __setitem__(self, index, value):
        self.data[index] = value

ml = MyList()
ml.data = [10, 20, 30]
print(ml[1])  # 20
ml[1] = 99
print(ml.data)  # [10, 99, 30]
print("========================================")
#__call__ → Objek bisa dipanggil seperti fungsi
class Greeter:
    def __call__(self, name):
        print(f"Halo {name}!")

g = Greeter()
g("Rudi")  # Halo Rudi!
print("========================================")
#__eq__ & __lt__ → Perbandingan objek
class Angka:
    def __init__(self, nilai):
        self.nilai = nilai
    def __eq__(self, other):
        return self.nilai == other.nilai
    def __lt__(self, other):
        return self.nilai < other.nilai

a = Angka(5)
b = Angka(7)
print(a == b)  # False
print(a < b)   # True
print("================================================")
# __enter__ & __exit__ → Context manager (with)
class FileOpener:
    def __enter__(self):
        print("Buka file")
    def __exit__(self, exc_type, exc_value, traceback):
        print("Tutup file")

with FileOpener():
    print("Proses file...")




































































































