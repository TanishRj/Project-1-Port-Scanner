'''
1. Timeout Function [DONE]
2. domain to ip convertor [DONE]
3. Multiple Targets []
4. Banner Details []
'''

import socket
from IPy import *

print("------------| PROJECT - 1 | BY TANISH CHOUDHARY |------------")

def ipcheck(ipaddress):
    try:
        IP(ipaddress)
        return ipaddress
    except ValueError:
        real_ip = socket.gethostbyname(ipaddress)
        return real_ip
    

def scan_trgt(ipaddress):
    real_ip = ipcheck(ipaddress)
    print(f"\n [+ | +] SCANNING TARGET {ipaddress}: ",real_ip)
    for port in range(1,100):
        scan_target(real_ip,port)

def scan_target(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.1)
        sock.connect((ipaddress, port))
        print(f"[+] Port {port} Is Open")
    except:
        # print("[-] Port ",port," Is Closed")
        pass
        

targets = input("Enter Target/s Address (for multiple addresses ,): ")
if ',' in targets:
    for target in targets.split(','):
        scan_trgt(target.strip(' '))
else:
    scan_trgt(targets)