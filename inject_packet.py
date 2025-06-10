from scapy.all import *

# Hedef IP ve Port
target_ip = "127.0.0.1"
target_port = 5001

# UDP Payload (içerik)
payload = b"Injected packet from Scapy!"

# Paket oluşturuluyor
packet = IP(dst=target_ip) / UDP(dport=target_port, sport=12345) / Raw(load=payload)

# Gönderim
send(packet, verbose=1)

print("[✅] Paket başarıyla inject edildi.")
