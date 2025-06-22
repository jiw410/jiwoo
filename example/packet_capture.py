from scapy.all import *
def packet_callback(packet):
    print(f"캡쳐된 패킷: {packet.summary()}")
sniff(prn=packet_callback)