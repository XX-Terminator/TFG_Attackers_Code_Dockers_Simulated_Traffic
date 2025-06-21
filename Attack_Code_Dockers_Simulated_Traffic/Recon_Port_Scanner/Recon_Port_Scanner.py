import socket
import time

TARGET_IP = "10.0.2.15"  # IP del broker (o máquina a escanear)
PORTS = [1883, 22, 80, 443, 8883]  # Puertos a escanear

def scan_port(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((ip, port))
    if result == 0:
        print(f"[+] Port {port} is OPEN")
    else:
        print(f"[-] Port {port} is CLOSED")
    s.close()

def port_scan():
    print(f"[*] Starting Port Scan on {TARGET_IP}")
    for port in PORTS:
        scan_port(TARGET_IP, port)
    print(f"[*] Scan complete.\n")

if __name__ == "__main__":
    while True:  # <-- Este es el bucle
        port_scan()
        time.sleep(0.07) 
    
