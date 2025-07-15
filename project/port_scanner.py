import socket


def port_scanner(ip, start_port, end_port):
    print(f"Scanning {ip} dari port {start_port} sampai {end_port}...\n")

    for port in range(start_port, end_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)  # Biar gak nunggu lama
        result = s.connect_ex((ip, port))  # 0 = berhasil terhubung (port terbuka)

        if result == 0:
            print(f"[+] Port {port} TERBUKA")
        s.close()



target_ip = input("Masukkan IP target: ")
start = int(input("Dari port: "))
end = int(input("Sampai port: "))

port_scanner(target_ip, start, end)
