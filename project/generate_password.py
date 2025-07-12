import random
import string



def generate_password(panjang):
    karakter = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(karakter) for _ in range(panjang))
    return password

panjang = int(input("Masukan panjang password : "))
print("password : ", generate_password(panjang))

