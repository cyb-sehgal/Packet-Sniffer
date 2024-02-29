
# Network Sniffer with Python and Scapy

## Overview
This project provides a simple network sniffer script in Python, utilizing the Scapy library. The script captures Ethernet and IP information from packets, allowing users to analyze network traffic. The script has been tested with the TP-Link TL-WN722N network adapter.

## Requirements
- Python 3.x
- Scapy library
## Installation
1. Clone the repository :

```bash
https://github.com/cyb-sehgal/Packet-Sniffer.git
```
```bash
cd Packet-Sniffer
```
2. Create a virtual environment (optional but recommended):
```bash
python3 -m venv venv
source venv/bin/activate  
```
- Activate on Linux/Mac
- Or on Windows
- venv\Scripts\activate



## Additional Steps
Adjusting the Script
Filtering Packets: Modify the filter in sniffer.py to capture specific types of packets (e.g., "tcp", "udp", "icmp", etc.). Edit the filter parameter in the sniff function.

Adding Functionality: Extend the script to perform additional analysis or logging based on captured packets.

## Usage
Run the script :
```bash
sudo python sniffer.py
```
## Script Output
When the script captures a packet, it will display information about the Ethernet and IP layers of the packet. The output will look like this:
```bash
Source MAC: xx:xx:xx:xx:xx:xx -> Destination MAC: yy:yy:yy:yy:yy:yy | EtherType: 0x800
    IP Packet: 192.168.1.100 -> 8.8.8.8

```
## That's it! Your network sniffer is now set up and ready to capture and analyze network traffic.
## Project Features :
- Captures Ethernet and IP information of network packets.
- Supports filtering by packet type (e.g., "tcp", "udp", "icmp").
- Displays source and destination MAC addresses.
- Shows source and destination IP addresses.
- Utilizes Scapy for packet manipulation and analysis.

## Author

- [@ Rahul Sehgal](https://github.com/cyb-sehgal)

## License

[MIT](https://choosealicense.com/licenses/mit/)

