import random
import string
import socket



def program():
    pilihan = input("====Pilih Opsi====\n"
                    "[1] Generate password\n"
                    "[2] IP generate\n"
                    "[3] Kalkulator \n"
                    "Masukan pilihan :")

    if pilihan == '1':
        def generate_password(panjang):
            karakter = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(karakter) for _ in range(panjang))
            return password

        panjang = int(input("Masukan panjang password : "))
        print("password : ", generate_password(panjang))
    elif pilihan == '2':
        hostname = input("Masukkan nama host : ")
        ip = socket.gethostbyname(hostname)
        print(f"IP address dari {hostname} adalah :{ip}")
    elif pilihan == '3':

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


    else:
        print(" tidak valid")
        return
program()