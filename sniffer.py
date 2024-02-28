# Import necessary libraries
from scapy.all import sniff

# Define the callback function to process sniffed packets
def packet_callback(packet):
    if packet.haslayer('Ethernet'):
        mac_src = packet['Ethernet'].src
        mac_dst = packet['Ethernet'].dst
        ether_type = hex(packet['Ethernet'].type)
        print(f"Source MAC: {mac_src} -> Destination MAC: {mac_dst} | EtherType: {ether_type}")

    if packet.haslayer('IP'):
        ip_src = packet['IP'].src
        ip_dst = packet['IP'].dst
        print(f"    IP Packet: {ip_src} -> {ip_dst}")

# Start sniffing packets
# You can adjust the filter as needed, e.g., "tcp", "udp", etc.
sniff(filter="ip", prn=packet_callback, store=0)
