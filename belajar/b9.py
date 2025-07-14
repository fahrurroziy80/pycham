#Bitwise DAN ( & ): Mengembalikan 1 jika kedua bit yang sesuai adalah 1; jika tidak, ia mengembalikan 0.
result = 10 & 7  # Binary: 1010 & 0111 = 0010 (Decimal: 2)
print(result)
# Bitwise ATAU ( | ): Mengembalikan 1 jika setidaknya satu bit yang sesuai adalah 1; jika tidak, ia mengembalikan 0
result = 10 | 7  # Binary: 1010 | 0111 = 1111 (Decimal: 15)
print(result)
#Bitwise XOR ( ^ ): Mengembalikan 1 jika hanya satu bit yang sesuai adalah 1 (yaitu, keduanya berbeda); jika tidak, ia mengembalikan 0.
result = 10 ^ 7  # Binary: 1010 ^ 0111 = 1101 (Decimal: 13)
print(result)
#Bitwise TIDAK ( ~ ): Membalikkan semua bit suatu angka. Operasi ini setara dengan -(x + 1) .
result = ~10  # Binary: ~0000 1010 = 1111 0101 (Decimal: -11)
print(result)
#Shift Kiri ( << ): Menggeser bit suatu angka ke kiri sejumlah posisi tertentu, mengisi posisi kosong dengan nol. Ini sama saja dengan mengalikan angka tersebut dengan 2 pangkat jumlah pergeseran.
result = 10 << 2  # Binary: 1010 << 2 = 101000 (Decimal: 40)
print(result)
#Shift Kanan ( >> ): Menggeser bit suatu angka ke kanan dengan jumlah posisi tertentu. Untuk bilangan positif, ia mengisi posisi kosong dengan angka nol. Untuk bilangan negatif, biasanya diisi dengan angka satu (ekstensi tanda) untuk mempertahankan tanda. Ini setara dengan pembagian bilangan bulat dengan 2 dipangkatkan dengan jumlah pergeseran.
result = 10 >> 1  # Binary: 1010 >> 1 = 0101 (Decimal: 5)//
print(result)



# operator assigmet
a = 5#aassigment
a += a
print(a)

a = 5
a -= a
print(a)

a = 5
a //= a
print(a)

a = 5
a *= a
print(a)



