from rakpy.protocol.Packet import Packet
from rakpy.protocol.PacketIdentifiers import PacketIdentifiers

class UnconnectedPing(Packet):
    PID = PacketIdentifiers.UnconnectedPing
    
    time = None
    clientID = None
    
    def encodePayload(self):
        self.putLong(time)
        self.putMagic()
        self.putLong(clientID)
        
    def decodePayload(self):
        time = self.getLong()
        magic = self.getMagic()
        clientID = self.getLong()
    
