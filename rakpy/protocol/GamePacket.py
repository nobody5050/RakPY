from rakpy.protocol.Packet import Packet
from rakpy.protocol.PacketIdentifiers import PacketIdentifiers

class GamePacket(Packet):
    id = PacketIdentifiers.GamePacket
    
    body = None
    
    def encodePayload(self):
        self.putByte(self.body)
        
    def decodePayload(self):
        self.body = self.getByte()
