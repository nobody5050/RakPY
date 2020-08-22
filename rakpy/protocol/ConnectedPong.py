from rakpy.protocol.Packet import Packet
from rakpy.protocol.PacketIdentifiers import PacketIdentifiers

class ConnectedPong(Packet):
    PID = PacketIdentifiers.ConnectedPong
    
    pingTime = None
    pongTime = None
    
    def encodePayload(self):
        self.putLong(pingTime)
        self.putLong(pongTime)
        
    def decodePayload(self):
        pingTime = self.getLong()
        pongTime = self.getLong()
