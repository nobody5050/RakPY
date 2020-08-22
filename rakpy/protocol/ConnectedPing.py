from rakpy.protocol.Packet import Packet
from rakpy.protocol.PacketIdentifiers import PacketIdentifiers

class ConnectedPing(Packet):
    PID = PacketIdentifiers.ConnectedPing
    
    time = None
    
    def encodePayload(self):
        self.putLong(time)
        
    def decodePayload(self):
        time = self.getLong()
