def hitung_mundur(n):
    if n == 0:
        print("selesai!")
        return
    print(n )
    hitung_mundur(n - 1)

hitung_mundur(8)
