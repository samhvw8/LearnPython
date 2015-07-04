import socket

def checkport(ip_address, port):

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        s.connect((ip_address, port))
        s.close()
    except:
        return False

    return True
