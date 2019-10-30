from netfilterqueue import NetfilterQueue
from scapy.all import *

def print_and_accept(pkt):
    print("Received " + str(pkt))
    ip = IP(pkt.get_payload())
    if (ip.haslayer("Raw")):
        old_payload = ip["Raw"].load
        # print(old_payload)
        if (old_payload[0] == 0x16 and old_payload[5] == 0x01):
            print(46,47,old_payload[46], old_payload[47])
            new_payload = [b for b in old_payload]

            new_payload[46] = 0x00
            new_payload[4] = 0x2f
            pkt.set_payload(bytes(new_payload))


    pkt.accept()

nfqueue = NetfilterQueue()
nfqueue.bind(1, print_and_accept)
try:
    nfqueue.run()
except KeyboardInterrupt:
    print('')

nfqueue.unbind()
