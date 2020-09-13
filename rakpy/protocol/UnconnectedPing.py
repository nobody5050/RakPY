from rakpy.protocol.Packet import Packet
from rakpy.protocol.PacketIdentifiers import PacketIdentifiers

class UnconnectedPing(Packet):
    id = PacketIdentifiers.UnconnectedPing
    
    timeStamp = None
    clientId = None
    
    def encodePayload(self):
        self.putLong(self.timeStamp)
        self.putMagic()
        self.putLong(self.clientId)
        
    def decodePayload(self):
        self.timeStamp = self.getLong()
        self.magic = self.getMagic()
        self.clientId = self.getLong()
    
