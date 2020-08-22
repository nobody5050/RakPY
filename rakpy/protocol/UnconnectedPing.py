from rakpy.protocol.Packet import Packet

class UnconnectedPing(Packet):
    PID = 0x01
    
    time = None
    magic = None
    clientID = None
    
    def encodePayload(self):
        self.putLong(time)
        self.putMagic()
        self.putLong(clientID)
        
    def decodePayload(self):
        time = self.getLong()
        magic = self.getMagic
        clientID = self.getLong
    
