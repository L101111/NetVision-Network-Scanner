import socket
import sys
from termcolor import colored, cprint

try:

    ex1=colored('$ python3 NetVision.py 192.168.126.129 21/1000', 'blue')
    ex2=colored('$ python3 NetVision.py 192.168.126.129 -p-', 'blue')
    ex3=colored('Ctrl+C', 'red')
    logo=colored(''' 

                     | \ | | ___| |\ \   / (_)___(_) ___  _ __  
                     |  \| |/ _ \ __\ \ / /| / __| |/ _ \| '_ \ 
                     | |\  |  __/ |_ \ V / | \__ \ | (_) | | | |
                     |_| \_|\___|\__| \_/  |_|___/_|\___/|_| |_|
                                            Made by hei$enberg  

    ''', 'blue')
    if sys.argv[1]=='-h' or sys.argv[1]=='--help' or sys.argv[1]=='help':
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
        sys.exit()

    ports_and_protocols = [
        20, 'FTP',
        21, 'FTP',
        22, 'SSH',
        23, 'Telnet',
        25, 'SMTP',
        53, 'DNS',
        67, 'DHCP Server',
        68, 'DHCP Client',
        80, 'HTTP',
        110, 'POP3',
        119, 'NNTP',
        123, 'NTP',
        143, 'IMAP',
        161, 'SNMP',
        194, 'IRC',
        443, 'HTTPS',
        465, 'SMTPS',
        993, 'IMAPS',
        995, 'POP3S',
        1433, 'MSSQL',
        3306, 'MySQL',
        3389, 'RDP',
        5432, 'PostgreSQL',
        5900, 'VNC',
    ]

    ip_addr = sys.argv[1]
    ports = sys.argv[2]
    open_p = []

    cprint("""


    ███╗   ██╗███████╗████████╗██╗   ██╗██╗███████╗██╗ ██████╗ ███╗   ██╗
    ████╗  ██║██╔════╝╚══██╔══╝██║   ██║██║██╔════╝██║██╔═══██╗████╗  ██║
    ██╔██╗ ██║█████╗     ██║   ██║   ██║██║███████╗██║██║   ██║██╔██╗ ██║
    ██║╚██╗██║██╔══╝     ██║   ╚██╗ ██╔╝██║╚════██║██║██║   ██║██║╚██╗██║
    ██║ ╚████║███████╗   ██║    ╚████╔╝ ██║███████║██║╚██████╔╝██║ ╚████║
    ╚═╝  ╚═══╝╚══════╝   ╚═╝     ╚═══╝  ╚═╝╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝
                                                       Made by hei$enberg

                                   
    """, "blue")



    if ports!='-p-':
        try:
            ports0 = ports.split('/')
            port_min = int(ports0[0])
            port_max = int(ports0[1])
        except (ValueError, IndexError):
            port_min = port_max = int(ports)

        

        for port in range(port_min, port_max + 1):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as xndzor:
                xndzor.settimeout(0.5)
                try:
                    xndzor.connect((ip_addr, port))
                    open_p.append(port)
                except (ConnectionRefusedError, TimeoutError, Exception):
                    pass
    else:
        for port in range(1,65536):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as xndzor:
                xndzor.settimeout(0.5)
                try:
                    xndzor.connect((ip_addr, port))
                    open_p.append(port)
                except (ConnectionRefusedError, TimeoutError, Exception):
                    pass

    if len(open_p)>0:
        cprint(f'SCAN RESULTS FOR {ip_addr}', 'yellow')
        print(' ')
        cprint("{:<10} {:<15} {:<10}".format('PORT', 'PROTOCOL', 'STATE'), 'blue')
        print(' ')
        for port in open_p:
            for i in range(0, len(ports_and_protocols), 2):
                if ports_and_protocols[i] == port:
                    pr=ports_and_protocols[i + 1]
            print("{:<10} {:<15} {:<10}".format(port, pr, 'OPEN'))
        print(' ')
        cprint('    scan complete', 'blue')
    else:
        print(' ')
        cprint('    no ports were found:( ', 'red')
except IndexError:
    print(' ')
    cprint('    wrong parameters...', 'red')

except KeyboardInterrupt:
    print(' ')
    cprint('    exiting ...', 'red')

