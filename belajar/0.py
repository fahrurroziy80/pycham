from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
import hashlib
import random
import string
import socket
import requests
import os

def tools():
    opsi = input("=====PILIHAN=====\n"
                 "[1]. Hasing Password\n"
                 "[2]. Generating Rendom Password\n"
                 "[3]. Network Scanning \n"
                 "[4]. Web Scanning \n"
                 "[5]. Password Craking\n"
                 "[6]. Secure File Handling\n"
                 "Masukan Pilihan: ")

    if opsi == "1":


        def hash_password(password, algorithm='sha256'):
            if algorithm == 'md5':
                hashed = hashlib.md5(password.encode()).hexdigest()
            elif algorithm == 'sha1':
                hashed = hashlib.sha1(password.encode()).hexdigest()
            elif algorithm == 'sha256':
                hashed = hashlib.sha256(password.encode()).hexdigest()
            elif algorithm == 'sha512':
                hashed = hashlib.sha512(password.encode()).hexdigest()
            else:
                raise ValueError("Algoritma tidak dikenali.")
            return hashed

        def main():
            print("=== Password Hasher Tool ===")
            password = input("Masukkan password yang ingin di-hash: ")

            print("\nPilih Algoritma Hashing:")
            print("1. MD5")
            print("2. SHA-1")
            print("3. SHA-256")
            print("4. SHA-512")

            opsi = input("Masukkan pilihan (1/2/3/4): ")

            algo_map = {
                '1': 'md5',
                '2': 'sha1',
                '3': 'sha256',
                '4': 'sha512'
            }

            if opsi in algo_map:
                algorithm = algo_map[opsi]
                hashed = hash_password(password, algorithm)
                print(f"\nHasil {algorithm.upper()} Hash: {hashed}")
            else:
                print("Pilihan tidak valid!")

        if __name__ == "__main__":
            main()


    elif opsi == "2":

        def generate_password(length, use_uppercase=True, use_lowercase=True, use_digits=True, use_symbols=True):
            characters = ''
            if use_uppercase:
                characters += string.ascii_uppercase
            if use_lowercase:
                characters += string.ascii_lowercase
            if use_digits:
                characters += string.digits
            if use_symbols:
                characters += string.punctuation

            if not characters:
                raise ValueError("Harus memilih minimal satu jenis karakter!")

            password = ''.join(random.choice(characters) for _ in range(length))
            return password

        def main():
            print("=== Random Password Generator ===")
            try:
                length = int(input("Masukkan panjang password: "))
            except ValueError:
                print("Input harus angka!")
                return

            print("\nPilih karakter yang akan digunakan:")
            use_uppercase = input("Gunakan Huruf Besar? (y/n): ").lower() == 'y'
            use_lowercase = input("Gunakan Huruf Kecil? (y/n): ").lower() == 'y'
            use_digits = input("Gunakan Angka? (y/n): ").lower() == 'y'
            use_symbols = input("Gunakan Simbol? (y/n): ").lower() == 'y'

            try:
                password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_symbols)
                print(f"\nPassword Random: {password}")
            except ValueError as e:
                print(e)

        if __name__ == "__main__":
            main()

    elif opsi == "3":

        def scan_ports(target_ip, start_port, end_port):
            print(f"Scanning target {target_ip} dari port {start_port} sampai {end_port}...\n")

            open_ports = []
            for port in range(start_port, end_port + 1):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(0.5)  # Waktu timeout (biar cepat)
                result = s.connect_ex((target_ip, port))
                if result == 0:
                    print(f"Port {port} is OPEN")
                    open_ports.append(port)
                s.close()

            if not open_ports:
                print("Tidak ada port terbuka ditemukan.")
            else:
                print(f"\nPort yang terbuka: {open_ports}")

        def main():
            print("=== Simple Network Port Scanner ===")
            target_ip = input("Masukkan IP target: ")

            try:
                start_port = int(input("Port mulai: "))
                end_port = int(input("Port akhir: "))
            except ValueError:
                print("Input port harus angka!")
                return

            scan_ports(target_ip, start_port, end_port)

        if __name__ == "__main__":
            main()

    elif opsi == "4":

        # List direktori umum untuk bruteforce
        common_directories = [
            'admin', 'login', 'dashboard', 'uploads', 'config', 'backup', 'test'
        ]

        # Mengecek status kode HTTP
        def check_status(url):
            try:
                response = requests.get(url)
                print(f"[{response.status_code}] {url}")
            except requests.exceptions.RequestException:
                print(f"[Error] Tidak bisa mengakses {url}")

        # Bruteforce direktori umum
        def directory_bruteforce(base_url):
            print("\n=== Directory Bruteforce ===")
            for directory in common_directories:
                url = f"{base_url}/{directory}"
                check_status(url)

        # Simple XSS Reflection Test
        def xss_test(url, param):
            print("\n=== XSS Reflection Test ===")
            payload = "<script>alert('XSS')</script>"
            try:
                response = requests.get(url, params={param: payload})
                if payload in response.text:
                    print(f"[VULNERABLE] Payload reflected at {url}?{param}=")
                else:
                    print(f"[SAFE] Payload not reflected.")
            except requests.exceptions.RequestException:
                print(f"[Error] Tidak bisa mengakses {url}")

        def main():
            print("=== Simple Web Scanner ===")
            target_url = input("Masukkan target URL (contoh: http://example.com): ")

            # Cek status halaman utama
            print("\n=== Checking Main Page Status ===")
            check_status(target_url)

            # Bruteforce direktori
            directory_bruteforce(target_url)

            # Simple XSS Testing
            test_xss = input("\nMau lakukan XSS Reflection Test? (y/n): ").lower()
            if test_xss == 'y':
                param = input("Masukkan nama parameter GET (contoh: search): ")
                xss_test(target_url, param)

        if __name__ == "__main__":
            main()

    elif opsi == "5":

        def hash_string(string, algorithm):
            if algorithm == 'md5':
                return hashlib.md5(string.encode()).hexdigest()
            elif algorithm == 'sha1':
                return hashlib.sha1(string.encode()).hexdigest()
            elif algorithm == 'sha256':
                return hashlib.sha256(string.encode()).hexdigest()
            else:
                raise ValueError("Algoritma hash tidak didukung.")

        def crack_password(hash_to_crack, wordlist_file, algorithm):
            try:
                with open(wordlist_file, 'r') as file:
                    passwords = file.readlines()
            except FileNotFoundError:
                print("Wordlist file tidak ditemukan.")
                return

            print(f"Mulai cracking menggunakan {algorithm.upper()}...")
            for word in passwords:
                word = word.strip()
                hashed_word = hash_string(word, algorithm)

                if hashed_word == hash_to_crack:
                    print(f"\n[FOUND] Password ditemukan: {word}")
                    return

            print("\nPassword tidak ditemukan di wordlist.")

        def main():
            print("=== Password Hash Cracker ===")
            hash_to_crack = input("Masukkan hash target: ")

            print("\nPilih Algoritma Hash:")
            print("1. MD5")
            print("2. SHA-1")
            print("3. SHA-256")

            opsi = input("Pilihan (1/2/3): ")
            algo_map = {'1': 'md5', '2': 'sha1', '3': 'sha256'}

            if opsi not in algo_map:
                print("Pilihan tidak valid.")
                return

            wordlist_file = input("Masukkan nama file wordlist (contoh: wordlist.txt): ")

            crack_password(hash_to_crack, wordlist_file, algo_map[opsi])

        if __name__ == "__main__":
            main()

    elif opsi == "6":

        # Padding untuk data agar sesuai block AES
        def pad(data):
            while len(data) % 16 != 0:
                data += b' '
            return data

        # Encrypt File
        def encrypt_file(file_name, key):
            cipher = AES.new(key, AES.MODE_ECB)

            with open(file_name, 'rb') as file:
                data = file.read()

            encrypted_data = cipher.encrypt(pad(data))

            with open(file_name + ".enc", 'wb') as enc_file:
                enc_file.write(encrypted_data)

            print(f"File berhasil dienkripsi: {file_name}.enc")

        # Decrypt File
        def decrypt_file(enc_file_name, key):
            cipher = AES.new(key, AES.MODE_ECB)

            with open(enc_file_name, 'rb') as file:
                encrypted_data = file.read()

            decrypted_data = cipher.decrypt(encrypted_data)

            original_file = enc_file_name.replace(".enc", "_decrypted")
            with open(original_file, 'wb') as dec_file:
                dec_file.write(decrypted_data.strip())

            print(f"File berhasil didekripsi: {original_file}")

        # Main Program
        def main():
            print("=== Secure File Handling Tool ===")
            print("1. Encrypt File")
            print("2. Decrypt File")
            choice = input("Pilih (1/2): ")

            if choice not in ['1', '2']:
                print("Pilihan tidak valid!")
                return

            file_name = input("Masukkan nama file: ")

            if not os.path.exists(file_name):
                print("File tidak ditemukan!")
                return

            key_input = input("Masukkan kunci (16 karakter): ")
            if len(key_input) != 16:
                print("Kunci harus 16 karakter!")
                return

            key = key_input.encode()

            if choice == '1':
                encrypt_file(file_name, key)
            elif choice == '2':
                decrypt_file(file_name, key)

        if __name__ == "__main__":
            main()

    else:
        print("pilihan tidak valid ")
        return


tools()