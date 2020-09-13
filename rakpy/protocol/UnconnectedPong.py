from rakpy.protocol.Packet import Packet
from rakpy.protocol.PacketIdentifiers import PacketIdentifiers

class UnconnectedPong(Packet):
    PID = PacketIdentifiers.UnconnectedPong
    
    timeStamp = None
    serverID = None
    serverName = None
    
    def encodePayload(self):
        self.putLong(self.timeStamp)
        self.putLong(self.serverID)
        self.putMagic()
        self.putString(self.serverName)
        
    def decodePayload(self):
        self.timeStamp = self.getLong()
        self.serverID = self.getLong()
        self.magic = self.getMagic()
        self.serverName = self.getString()
