import paho.mqtt.client as mqtt
import time
import random
import string

BROKER = "10.0.2.15"  # Cambia según tu broker
PORT = 1883



def generate_random_topic():
    return "/sensor/" + ''.join(random.choices(string.ascii_lowercase, k=8))

try:
    client = mqtt.Client()
    client.connect(BROKER, PORT, 60)  # Conexion al broker
    client.loop_start()
    
    while True:
        topic = generate_random_topic()
        client.subscribe(topic)
        print(f"[+] Client subscribed to {topic}")
        time.sleep(0.01)  # Pequeño delay para evitar crashes
        
except Exception as e:
    print(f"[!] Error: {e}")
