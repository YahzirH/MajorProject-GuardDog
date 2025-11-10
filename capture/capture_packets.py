from scapy.all import sniff, wrpcap
import csv
from datetime import datetime
import os

os.makedirs("capture_logs", exist_ok=True)

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
pcap_file = f"capture_logs/capture_{timestamp}.pcap"
csv_file = f"capture_logs/capture_{timestamp}.csv"

packet_summaries = []

def process_packet(pkt):
    info = {}
    if pkt.haslayer("Ether"):
        info["src_mac"] = pkt.src
        info["dst_mac"] = pkt.dst
    if pkt.haslayer("IP"):
        info["src_ip"] = pkt["IP"].src
        info["dst_ip"] = pkt["IP"].dst
        info["protocol"] = pkt["IP"].proto
    else:
        info["protocol"] = pkt.summary().split()[0]
    info["timestamp"] = datetime.now().strftime("%H:%M:%S")
    packet_summaries.append(info)

def main():
   print("Capturing packets... Press Ctrl+C to stop.")
   packets = sniff(count=50, iface=None, prn=process_packet)

   wrpcap(pcap_file, packets)
   print(f"Saved raw packets to {pcap_file}")

   with open(csv_file, "w", newline="") as file:
       field_names = ["timestamp", "src_mac", "dst_mac", "src_ip", "dst_ip", "protocol"]
       writer = csv.DictWriter(file, fieldnames=field_names)
       writer.writeheader()
       writer.writerows(packet_summaries)

   print(f"Saved summary to {csv_file}")
   print("Capture complete.")

   file = 'capture_logs/capture_20251110_181845.csv'
   with open(file) as file:
       for line in file:
           print(line)


if __name__ == '__main__':
    main()