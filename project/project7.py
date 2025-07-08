from sys import hash_info


def kalkulator ():
    a = float(input("masukan angka pertama :"))
    b = float(input("masukan angka kedua : "))

    operator = input("pilih operasi : [+ , - , * , / ] : ")

    if operator == "+":
        hasil = a + b
    elif operator == "-":
        hasil = a - b
    elif operator == "*":
        hasil = a * b
    elif operator == "/":
        hasil = a / b
    else:
        print("oprasi tidak valid ")
        return

    print("adalah", hasil)
kalkulator()
kalkulator()
kalkulator()
kalkulator()
