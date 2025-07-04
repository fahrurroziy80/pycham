# def hitung_mundur(n):
#     if n == 0:
#         print("selesai!")
#         return
#     print(n )
#     hitung_mundur(n - 1)
#
# hitung_mundur(8)


# def hitung_mundur(n, a = 1):
#     if a > n  :
#         print("selesai!")
#         return
#     print(n,a)
#     hitung_mundur(n ,a + 1)
#
# hitung_mundur(100)


def tambah_angka (a, b = 1):
    if a == b:
        return
    print(b)
    tambah_angka(a, b + 1)

tambah_angka(10)
