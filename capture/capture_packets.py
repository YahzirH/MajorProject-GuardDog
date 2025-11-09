import pyshark

capture = pyshark.LiveCapture(interface='Wi-Fi')
capture.sniff(timeout=10)
packets = [pkt for pkt in capture._packets]
capture.close()
for packet in packets:
   print(packet)
