import socket
from common_ports import ports_and_services

def get_open_ports(target, port_range, verbose = False):
    if not verbose:
        open_ports = []
        for port in range(port_range[0], port_range[1]+1): 
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5) 
            if not s.connect_ex((target, port)):
                open_ports.append(port)
            s.close()
    else: 
        open_ports = f'Open ports for {target}\nPORT     SERVICE\n'
        for port in range(port_range[0], port_range[1]+1): 
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.4) 
            if not s.connect_ex((target, port)):
                open_ports += (f"{port}{' '*(9-len(str(port)))}{ports_and_services[port]}\n").rstrip()
            s.close()
    return(open_ports)