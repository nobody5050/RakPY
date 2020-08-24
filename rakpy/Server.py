from rakpy.protocol.ConnectedPing import ConnectedPing
from rakpy.protocol.ConnectedPong import ConnectedPong
from rakpy.protocol.UnconnectedPing import UnconnectedPing
from rakpy.protocol.UnconnectedPingOpenConnection import UnconnectedPingOpenConnection
from rakpy.protocol.UnconnectedPong import UnconnectedPong

class Server:
    def rawPacket(self, pid, packet):
        return bytes([pid]) + packet
    
    def getPID(self, data):
        return data[0]
    
    def handler(self, data, address):
        pid = getPID(data)
        pk = None
        if pid == 
    
