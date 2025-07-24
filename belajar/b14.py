#data end time (latihan)
import datetime as dt

hari_ini = dt.date.today()

print(hari_ini)
print(f"ini hari :{hari_ini:%A}")

print("==========================")

#input manual
tanggal = dt.date(2005,8,20)
print(tanggal)
print(f"Ini hari :{tanggal:%A}")

print("================================")
import datetime as dt

print("silakan masukan tanggal, bulan, tahun")

tanggal = input("masukan tanggal lahir anda :")
bulan = input("masukan bulan lahir anda : ")
tahun = input("masukan tahun lahir anda : ")

print("tanggal ",tanggal)
print("bulan",bulan)
print("tahun",tahun)