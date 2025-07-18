# def pengurutan():
#     data = [1,3,4,2,5,7,6,8,9]
#
#     data.sort()
#     print(data)
#
#     print("==menggunakan sorted==")
#
#     data_sorted = sorted(data)
#     print(data_sorted)
# pengurutan()

print("soal 1")
urutkan_data = [10, 3, 7, 1]
urutkan_data = sorted(urutkan_data)
print(urutkan_data)

print("soal 2")
urutkan_menurun  = [4, 9, 2, 1]
urutkan_menurun = sorted(urutkan_menurun, reverse=True)
print(urutkan_menurun)

print("soal 3")
list_nama = ["Zara", "Andi", "Lina", "Budi"]
list_nama = sorted(list_nama)
print(list_nama)

print("soal 4")
daftar_kata = ["pisang", "apel", "mangga", "kiwi", "lol"]
kata_terurut_panjang = sorted(daftar_kata, key=len, reverse=True)
print(kata_terurut_panjang)


print("soal 5")
list_tupel = [(3, "apel"), (1, "pisang"), (2, "jeruk")]
list_tupel = sorted(list_tupel)
print(list_tupel)

print("soal 6")

data = [1,3,4,2,5,7,6,8,9]
data.sort()
print(data)
print("==menggunakan sorted==")
data_sorted = sorted(data)
print(data_sorted)
