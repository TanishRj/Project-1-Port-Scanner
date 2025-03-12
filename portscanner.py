# Importing Libraries
import socket # For Connecting to Port
from IPy import * # Converting Domain to IP

print("------------| PROJECT - 1 | BY TANISH CHOUDHARY |------------")

# Function to convert domain to ip address
def ipcheck(ipaddress):
    try:
        IP(ipaddress)
        return ipaddress
    except ValueError:
        real_ip = socket.gethostbyname(ipaddress) # Conversion
        return real_ip
    
# Get information about service running on that port
def getbnr(sock):
    return sock.recv(1024)

# Scanning the multiple or single ip addresses for 100 ports
def scan_trgt(ipaddress):
    real_ip = ipcheck(ipaddress)
    print(f"\n [+ | +] SCANNING TARGET {ipaddress}: ",real_ip)
    for port in range(1,100):
        scan_target(real_ip,port)

# Checks the port is open or not and extract the service information
def scan_target(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.1) # Timeout for fast scanning
        sock.connect((ipaddress, port))
        # Banner Grabbing
        try:
            banner = getbnr(sock)
            print(f"[+] Port {port} is Open : {banner}")
        except:
            print(f"[+] Port {port} Is Open")
    except:
        # Not printing closed port for formatted results
        # print("[-] Port ",port," Is Closed")
        pass
        
# Entry of Program, takes the target/s as input
targets = input("Enter Target/s Address (for multiple addresses ,): ")
# Seperate the targets if multiple supplied
if ',' in targets:
    for target in targets.split(','):
        scan_trgt(target.strip(' '))
# Single target scan
else:
    scan_trgt(targets)