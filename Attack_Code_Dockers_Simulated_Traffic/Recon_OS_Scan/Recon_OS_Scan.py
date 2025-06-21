from scapy.all import IP, TCP, sr1
import sys
import time

TARGET = "10.0.2.15"  # IP del objetivo
PORT = 1883             # Puerto TCP (puede ser 80, 443, etc.)

def os_fingerprint(target, port):
    print(f"[+] Starting OS Scan on {target}:{port}")
   
    pkt = IP(dst=target)/TCP(dport=port, flags="S")
    response = sr1(pkt, timeout=2, verbose=0)
   
    if response is None:
        print("[!] No response received.")
        return
   
    # TTL Based OS Guessing
    ttl = response.ttl
    window_size = response[TCP].window
   
    print(f"[+] Received TTL: {ttl}")
    print(f"[+] TCP Window Size: {window_size}")
   
    # Simple fingerprinting logic
    if ttl <= 64:
        print("[+] OS Guess: Likely Linux/Unix")
    elif ttl <= 128:
        print("[+] OS Guess: Likely Windows")
    else:
        print("[+] OS Guess: Likely Networking Device (Router/Switch)")

    print("[+] Scan Complete.")


if __name__ == "__main__":
    while True:
        os_fingerprint(TARGET, PORT)

    
