from netfilterqueue import NetfilterQueue
from scapy.all import *

def print_and_accept(pkt):
    print(pkt)
    ip = IP(pkt.get_payload())

    if (ip.haslayer(Raw)):
        http = ip[Raw].load.decode()
        print(http)

    pkt.accept()

nfqueue = NetfilterQueue()
nfqueue.bind(1, print_and_accept)
try:
    nfqueue.run()
except KeyboardInterrupt:
    print('')

nfqueue.unbind()
