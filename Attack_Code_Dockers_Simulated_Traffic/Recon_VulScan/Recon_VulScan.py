import socket
import time

TARGET_IP = "10.0.2.15"  # IP del broker
PORTS = [21, 22, 80, 1883, 443, 3306]  # Puertos típicos a analizar

def banner_grab(ip, port):
    try:
        s = socket.socket()
        s.settimeout(2)
        s.connect((ip, port))
        banner = s.recv(1024).decode().strip()
        print(f"[+] {ip}:{port} Banner: {banner}")
        s.close()
    except socket.timeout:
        print(f"[-] {ip}:{port} No response (timeout)")
    except Exception as e:
        print(f"[-] {ip}:{port} Error: {e}")

if __name__ == "__main__":
    while True:
        print(f"[+] VulScan on {TARGET_IP}")
        for port in PORTS:
            banner_grab(TARGET_IP, port)
        print("[+] Waiting 60s for next scan...")
        time.sleep(1)
    
