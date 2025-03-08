# Importing Libraries
import socket
from IPy import IP

print("--------------| PROJECT - 1 : By Tanish Choudhary |--------------")

# Scanning Multiple Targets
def scan(target):
    converted_ip = check_ip(target) # Returing Ip if domain provided
    print('\n' + '[+|+] Scanning Target] ' + str(target))
    for port in range(1,500):
        scan_port(converted_ip, port) # Function called for scanninng each target serperated by ','


# Function to return IP if domain or web link provided
def check_ip(ip):
    try:
        # Returns ip if Ip was provided
        IP(ip)
        return(ip)
    except ValueError:
        # return value of domain into IP 
        return socket.gethostbyname(ip)

# Grabbing Banner 
def get_banner(s):
    return s.recv(1024)

# Function for Scanning for open Ports
def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        # Timeout function for removing extra time to return port status
        sock.settimeout(0.5)
        sock.connect((ipaddress, port))
        try:
            banner = get_banner(sock)
            print('[+|+] OPEN PORT ' + str(port) + ' : ' + str(banner.decode().strip('\n')))
        except:
            print('[+|+] OPEN PORT ' + str(port))
    except:
        # Not Printing Closed Ports
        pass


# Main Function
if __name__ == "__main__": 
    # Getting all targets from user
    targets = input('[+|+] ENTER TARGETS TO SCAN (SEPERATE THEM BY ,): ')
    # Seperating Targets from ','
    if ',' in targets:
        for ip_add in targets.split(','):
            scan(ip_add.strip(' '))
    else:
        # Scanning if single target was provided
        scan(targets)

# Project Finished