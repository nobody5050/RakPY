from rakpy.protocol.Packet import Packet
from rakpy.protocol.PacketIdentifiers import PacketIdentifiers

class ConnectionRequestAccepted(Packet):
    id = PacketIdentifiers.ConnectionRequestAccepted
    
    clientAddress = None
    systemIndex = None
    internalId = None
    requestTime = None
    time = None
    
    def encodePayload(self):
        self.putAddress(self.clientAddress)
        self.putShort(self.systemIndex)
        
        self.putLong(self.requestTime)
        self.putLong(self.time)
        
    def decodePayload(self):
        self.clientAddress = self.getAddress()
        self.systemIndex = self.getShort()
        
        self.requestTime = self.getLong()
        self.time = self.getLong()
