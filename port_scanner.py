import socket
from concurrent.futures import ThreadPoolExecutor

target_ip = "192.168.1.1"

ports = [21, 22, 23, 80, 443, 8080]

def scan_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))
            if result == 0:
                print(f"Port {port} is open on {ip}")
            else:
                print(f"Port {port} is closed on {ip}")
    except Exception as e:
        print(f"Error connecting to port {port} on {ip}: {e}")


with ThreadPoolExecutor(max_workers=10) as executor:
    for port in ports:
        executor.submit(scan_port, target_ip, port)
