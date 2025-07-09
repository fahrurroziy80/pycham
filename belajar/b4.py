import socket

def cek_ip_host():
    print("=== TOOLS CEK IP ADDRESS MULTI-HOST ===")
    print("Contoh input: google.com, youtube.com, github.com")

    # Ambil input domain, pisahkan dengan koma
    input_host = input("Masukkan host/domain: ")
    daftar_host = [host.strip() for host in input_host.split(',')]

    print("\nHasil:")
    print("{:<25} {:<20}".format("Hostname", "IP Address"))
    print("-" * 45)

    for host in daftar_host:
        try:
            ip = socket.gethostbyname(host)
            print("{:<25} {:<20}".format(host, ip))
        except socket.gaierror:
            print("{:<25} {:<20}".format(host, "Gagal Mendapatkan IP"))


cek_ip_host()
