


def kalkulator():
    a = float(input("masukan angka 1 :"))
    b = float(input("masukan angka 2 :"))

    operator = input("pilih operasi : [*], [/], [+], [-] : ")

    if operator == "*":
        hasil = a * b
    elif operator == "/":
        hasil = a / b
    elif operator == "+":
        hasil = a + b
    elif operator == "-":
        hasil = a - b
    else:
        print("operasi tidak valid")
        return
    print("hasilnya adalah : ", hasil)

kalkulator()