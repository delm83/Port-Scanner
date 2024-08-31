import socket
from common_ports import ports_and_services

def get_open_ports(target, port_range, verbose = False):
    # test if url or ip address is valid
    try:
        socket.getaddrinfo(target, 80)
    except:
        return "Error: Invalid IP address" if target.replace('.', '').isnumeric() else "Error: Invalid hostname"
    
    if not verbose:
        open_ports = []
    else: 
        #check if target is ip address or url
        if target.replace('.', '').isnumeric():
            try:
                hostname = socket.gethostbyaddr(target)[0]
            except:
                hostname = False
            open_ports = f'Open ports for {hostname} ({(target)})\nPORT     SERVICE' if hostname else f'Open ports for {target}\nPORT     SERVICE'
        else: 
            open_ports = f'Open ports for {target} ({socket.gethostbyname(target)})\nPORT     SERVICE'
    for port in range(port_range[0], port_range[1]+1): 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.6) 
        if not s.connect_ex((target, port)):
            if verbose:
                open_ports += (f"\n{port}{' '*(9-len(str(port)))}{ports_and_services[port]}").rstrip()
            else: open_ports.append(port)
        s.close()
    return(open_ports)