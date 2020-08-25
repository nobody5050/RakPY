from rakpy.protocol.Packet import Packet
from rakpy.protocol.PacketIdentifiers import PacketIdentifiers

class UnconnectedPong(Packet):
    PID = PacketIdentifiers.UnconnectedPong
    
    time = None
    serverID = None
    serverIDString = None
    
    def encodePayload(self):
        self.putLong(self.time)
        self.putLong(self.serverID)
        self.putMagic()
        self.putString(self.serverIDString)
        
    def decodePayload(self):
        self.time = self.getLong()
        self.serverID = self.getLong()
        self.magic = self.getMagic()
        self.serverIDString = self.getString()
