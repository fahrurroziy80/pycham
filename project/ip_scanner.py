import socket

hostname = input("Masukkan nama host : ")
ip = socket.gethostbyname(hostname)
print(f"IP address dari {hostname} adalah :{ip}")
