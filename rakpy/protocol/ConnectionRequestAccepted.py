from rakpy.InternetAddress import InternetAddress
from rakpy.protocol.Packet import Packet
from rakpy.protocol.PacketIdentifiers import PacketIdentifiers

class ConnectionRequestAccepted(Packet):
    id = PacketIdentifiers.ConnectionRequestAccepted
    
    clientAddress = None
    systemIndex = None
    internalId = []
    requestTime = None
    time = None
    
    def encodePayload(self):
        self.putAddress(self.clientAddress)
        self.putShort(self.systemIndex)
        for i in range(0, 20):
            self.putAddress(self.internalId[i] if len(test) > i else InternetAddress("127.0.0.1", 0, 4))
        self.putLong(self.requestTime)
        self.putLong(self.time)
        
    def decodePayload(self):
        self.clientAddress = self.getAddress()
        self.systemIndex = self.getShort()
        for i in range(0, 20):
            self.internalId.append(self.getAddress() if self.getOffset + 16 < len(self.getBuffer()) else InternetAddress("127.0.0.1", 0, 4))
        self.requestTime = self.getLong()
        self.time = self.getLong()
