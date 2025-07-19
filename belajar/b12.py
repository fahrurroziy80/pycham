# # # Fungsi lambda untuk mengkuadratkan angka
# # kuadrat = lambda x: x * x
# # print(kuadrat(5))  # Output: 25
# #
# # # Menggunakan lambda dengan map
# # angka = [1,2,3,4,5]
# # kuadrat_angka = list(map(lambda x: x * x, angka))
# # print(kuadrat_angka)
#
#
# anngka_list = [6, 7, 8, 9, 10]
# kuadrat_angka = list(map(lambda x: x * x, anngka_list))
# print(kuadrat_angka)
#
#
# anngka_list = [1, 2, 3, 4, 5]
# kuadrat_angka1 = list(map(lambda x: x ** x, anngka_list))
# print(kuadrat_angka1)
#
# lis_str = ["python", "lambda", "map", "function"]
# kuadrat_angka2 = list(map(lambda x: x * x , lis_str))
# print(kuadrat_angka2)
#
#


angka = input("Masukkan angka-angka (pisahkan dengan koma): ")
angka = list(map(int, angka.split(",")))

kuadrat_angka = list(map(lambda x: x * x, angka))
print("Hasil kuadrat:", kuadrat_angka)
