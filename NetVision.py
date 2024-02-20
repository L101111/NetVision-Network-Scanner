import socket
import sys
from termcolor import colored, cprint


def print_help():
    ex1 = colored('$ python3 NetVision.py 192.168.126.129 21/1000', 'blue')
    ex2 = colored('$ python3 NetVision.py 192.168.126.129 -p-', 'blue')
    ex3 = colored('Ctrl+C', 'red')
    logo = colored(''' 
                     | \ | | ___| |\ \   / (_)___(_) ___  _ __  
                     |  \| |/ _ \ __\ \ / /| / __| |/ _ \| '_ \ 
                     | |\  |  __/ |_ \ V / | \__ \ | (_) | | | |
                     |_| \_|\___|\__| \_/  |_|___/_|\___/|_| |_|
                                            Made by hei$enberg  

    ''', 'blue')

    print(f'''                       
        {logo}
                    Welcome to NetVision Network Scanner!

                                    * * *

        To use this tool effectively, please specify the IP address and the range of ports:
                    
                {ex1}

        Or if you want to scan all ports simply add -p-:

                {ex2}

        To exit, simply press {ex3}

            
        An example of a scan:
    ''')

    cprint(''' 
        ***********************************
        SCAN RESULTS FOR 192.168.126.129
         
        PORT       PROTOCOL        STATE     
         
        21         FTP             OPEN      
        22         SSH             OPEN      
        23         Telnet          OPEN      
        25         SMTP            OPEN      
        53         DNS             OPEN      
        80         HTTP            OPEN      
        111        HTTP            OPEN      
        139        HTTP            OPEN      
        445        HTTP            OPEN      

                scan complete

            ''', 'yellow')

ports_and_protocols = {
        20: 'FTP',
        21: 'FTP',
        22: 'SSH',
        23: 'Telnet',
        25: 'SMTP',
        53: 'DNS',
        67: 'DHCP Server',
        68: 'DHCP Client',
        80: 'HTTP',
        110: 'POP3',
        119: 'NNTP',
        123: 'NTP',
        143: 'IMAP',
        161: 'SNMP',
        194: 'IRC',
        443: 'HTTPS',
        465: 'SMTPS',
        993: 'IMAPS',
        995: 'POP3S',
        1433: 'MSSQL',
        3306: 'MySQL',
        3389: 'RDP',
        5432: 'PostgreSQL',
        5900: 'VNC',
    }
def scan_ports(ip_addr, ports):
    cprint("""


███╗   ██╗███████╗████████╗██╗   ██╗██╗███████╗██╗ ██████╗ ███╗   ██╗
████╗  ██║██╔════╝╚══██╔══╝██║   ██║██║██╔════╝██║██╔═══██╗████╗  ██║
██╔██╗ ██║█████╗     ██║   ██║   ██║██║███████╗██║██║   ██║██╔██╗ ██║
██║╚██╗██║██╔══╝     ██║   ╚██╗ ██╔╝██║╚════██║██║██║   ██║██║╚██╗██║
██║ ╚████║███████╗   ██║    ╚████╔╝ ██║███████║██║╚██████╔╝██║ ╚████║
╚═╝  ╚═══╝╚══════╝   ╚═╝     ╚═══╝  ╚═╝╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝
                                                   Made by hei$enberg

                                   
""", "blue")
    
    open_ports = []

    if ports != '-p-':
        try:
            port_range = ports.split('/')
            port_min = int(port_range[0])
            port_max = int(port_range[1])
        except (ValueError, IndexError):
            port_min = port_max = int(ports)
    else:
        port_min = 1
        port_max = 65535

    for port in range(port_min, port_max + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            try:
                s.connect((ip_addr, port))
                open_ports.append(port)
            except (ConnectionRefusedError, TimeoutError):
                pass

    return open_ports


def print_scan_results(ip_addr, open_ports):
    if open_ports:
        cprint(f'SCAN RESULTS FOR {ip_addr}', 'yellow')
        print(' ')
        cprint("{:<10} {:<15} {:<10}".format('PORT', 'PROTOCOL', 'STATE'), 'blue')
        print(' ')
        for port in open_ports:
            protocol = ports_and_protocols.get(port, 'Unknown')
            print("{:<10} {:<15} {:<10}".format(port, protocol, 'OPEN'))
        print(' ')
        cprint('    scan complete', 'blue')
    else:
        print(' ')
        cprint('    no ports were found :( ', 'red')

def main():
    try:
        if len(sys.argv) == 2 and (sys.argv[1] == '-h' or sys.argv[1] == '--help' or sys.argv[1] == 'help'):
            print_help()
            sys.exit()
        elif len(sys.argv) != 3:
            raise IndexError

        ip_addr = sys.argv[1]
        ports = sys.argv[2]

        open_ports = scan_ports(ip_addr, ports)
        print_scan_results(ip_addr, open_ports)
    except IndexError:
        print(' ')
        cprint('    wrong parameters...', 'red')
    except KeyboardInterrupt:
        print(' ')
        cprint('    exiting ...', 'red')


if __name__ == "__main__":
    main()
