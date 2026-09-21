from scapy.all import *
import matplotlib.pyplot as plt

tcp_initial_sequence_number_list = []
tcp_source_ports_list = []

def tcp_sniffer(packet):
    if packet.haslayer(TCP):
        if packet[TCP].flags == 'S':
            tcp_initial_sequence_number_list.append(packet[TCP].seq)
            tcp_source_ports_list.append(packet[TCP].sport)
            print(packet[TCP].seq)

sniff(iface='\\Device\\NPF_Loopback', filter='tcp port 9999', count=100, timeout=30, prn=tcp_sniffer)

# Using matplotlib to build a graph illustrating randomisation of ISNs

x_values = range(len(tcp_initial_sequence_number_list))

plt.scatter(x_values,tcp_initial_sequence_number_list)
plt.xlabel('Capture Order')
plt.ylabel('Initial Sequence Number')
plt.title('TCP ISN Randomness')
plt.savefig('isn_chart.png')
plt.show()

# Using matplotlib again but this time, to demonstrate the randomization of source ports, which are one-fifth of the five-tuple that is hard for attackers to spoof in TCP connections.

plt.scatter(x_values, tcp_source_ports_list)
plt.xlabel('Capture Order')
plt.ylabel('Source Ports')
plt.title('Ephemeral Source Ports')
plt.savefig('source_port_chart.png')
plt.show()