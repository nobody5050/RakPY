from rakpy.protocol.Packet import Packet
from rakpy.protocol.PacketIdentifiers import PacketIdentifiers

class UnconnectedPong(Packet):
    id = PacketIdentifiers.UnconnectedPong
    
    timeStamp = None
    serverId = None
    serverName = None
    
    def encodePayload(self):
        self.putLong(self.timeStamp)
        self.putLong(self.serverId)
        self.putMagic()
        self.putString(self.serverName)
        
    def decodePayload(self):
        self.timeStamp = self.getLong()
        self.serverId = self.getLong()
        self.magic = self.getMagic()
        self.serverName = self.getString()
