import os
import platform
import subprocess
import time

# Configura el rango de red
network_prefix = "10.0.2."  # Por ejemplo, 10.0.2.X
start_ip = 1
end_ip = 254

# Detectar sistema operativo (Windows o Linux)
param = "-n" if platform.system().lower() == "windows" else "-c"

def ping_sweep():
    print("[*] Starting Ping Sweep...")

    for i in range(start_ip, end_ip + 1):
        ip = f"{network_prefix}{i}"
        try:
            # Ejecutar ping a cada IP
            output = subprocess.run(["ping", param, "1", ip], stdout=subprocess.DEVNULL)

            if output.returncode == 0:
                print(f"[+] Host {ip} is UP")
       
        except Exception as e:
            print(f"[!] Error pinging {ip}: {e}")

    print("[*] Ping Sweep completed.\n")

if __name__ == "__main__":
    while True:
        ping_sweep()
        
    
