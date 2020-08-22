from rakpy.protocol.Packet import Packet
from rakpy.protocol.PacketIdentifiers import PacketIdentifiers

class UnconnectedPong(Packet):
    PID = PacketIdentifiers.UnconnectedPong
    
    time = None
    serverID = None
    magic = None
    serverIDString = None
    
    def encodePayload(self):
        self.putLong(time)
        self.putLong(serverID)
        self.putMagic()
        self.putString(serverIDString)
        
    def decodePayload(self):
        time = self.getLong()
        serverID = self.getLong
        magic = self.getMagic
        serverIDString = self.getString
