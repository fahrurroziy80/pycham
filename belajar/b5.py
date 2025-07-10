print("==soal1==")
for i in range(1, 5):  # Baris dari 1 hingga 4
    for j in range(1, i + 1):  # Angka dari 1 hingga i
        print(j, end=" ")  # Cetak angka di baris yang sama
    print()  # Pindah ke baris berikutnya


print("==soal2==")
def luar():
    print("ini fungsi luar")

    def dalam():
        print("ini fungsi dalam")


    dalam()
luar()


print("==soal3==")

def jumlah (a):
    if a == 0:
        return 0
    return  a + jumlah(a - 1 )

print(jumlah(6))
