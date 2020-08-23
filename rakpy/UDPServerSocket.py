import socket

class UDPServerSocket:
    socket = None
    
    def __init__(self, ip: str, port: int):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        try:
            self.socket.bind((ip, port))
        except socket.error as e:
            print("Cannot use this port! Is a server already on it?")
            print(str(e))
        else:
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            self.socket.setblocking(False)
       
    def getPacket(self):
        try:
            data = self.socket.recvfrom(65535)
        except Exception as e:
            pass
        else:
            return data
          
    def putPacket(self, buffer, ip, port):
        return self.socket.sendto(buffer, (ip, port))
      
    def closeSocket(self):
        self.socket.close()
