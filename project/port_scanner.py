import socket


def get_service(port):
    try:
        return socket.getservbyport(port)
    except:
        return "Unknown Service"


def port_scanner(ip, start_port, end_port):
    print(f"\n🔎 Scanning {ip} dari port {start_port} sampai {end_port}...\n")

    for port in range(start_port, end_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)

        result = s.connect_ex((ip, port))

        if result == 0:
            service = get_service(port)
            print(f"[+] Port {port} TERBUKA → Layanan: {service}")

        s.close()


# Input dari pengguna
target_ip = input("Masukkan IP target: ")
start = int(input("Dari port: "))
end = int(input("Sampai port: "))

# Jalankan scanner
port_scanner(target_ip, start, end)
