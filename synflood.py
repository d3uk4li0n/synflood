from scapy.all import *
import os
import sys
import random
from colorama import Fore

def random_ip():
    return ".".join(str(random.randint(0, 255)) for _ in range(4))

def random_port():
    print(random.randrange(65535))
