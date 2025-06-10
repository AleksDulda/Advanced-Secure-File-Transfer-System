from scapy.all import IP, send

def send_custom_ip_packet(dst_ip):
    packet = IP(
        dst=dst_ip,
        ttl=2,
        flags='MF',
        id=12345
    ) / b'Test payload for header manipulation'

    packet = packet.__class__(bytes(packet))  # Checksum hesapla

    print("[*] IP Header:")
    print(f"  Destination: {packet[IP].dst}")
    print(f"  TTL:         {packet[IP].ttl}")
    print(f"  Flags:       {packet[IP].flags}")
    print(f"  Fragment ID: {packet[IP].id}")
    print(f"  Checksum:    {hex(packet[IP].chksum)}")  # hex format

    send(packet)

if __name__ == "__main__":
    send_custom_ip_packet("8.8.8.8")
