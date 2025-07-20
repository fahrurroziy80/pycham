def my_decorator(func):
    def wrapper():
        print("Menjalankan fungsi : ", say_hello)
        func()
        print("Setelah eksekusi fungsi")
    return wrapper

@my_decorator
def say_hello():
    print("Hello, decorator!")

say_hello()


print("=====================================================================")

class Kalkulator:
    @staticmethod
    def tambah(a, b):
        return a + b

print("hasilnya adalah =",Kalkulator.tambah(3, 5))  # Output: 8


print("================================================================")
class Mahasiswa:
    jumlah = 0

    def __init__(self, nama):
        self.nama = nama
        Mahasiswa.jumlah += 1

    @classmethod
    def total_mahasiswa(cls):
        return cls.jumlah

# Buat objek
m1 = Mahasiswa("Ani")
m2 = Mahasiswa("Budi")

print("hailnya adalah = ",Mahasiswa.total_mahasiswa())  # Output: 2

print("=========================================================================")
class Lingkaran:
    def __init__(self, jari):
        self._jari = jari

    @property
    def luas(self):
        return 3.14 * self._jari * self._jari

# Gunakan
ling = Lingkaran(7)
print("hasilnya adalah = ",ling.luas)  # Output: 153.86 (tanpa tanda kurung)
