from rakpy.protocol.Packet import Packet
from rakpy.protocol.PacketIdentifiers import PacketIdentifiers

class AcknowledgePacket(Packet):
    packets = []
    
    def encodePayload(self):
        records = 0
        self.packets.sort(key=int)
        count = len(self.packets)
        if count > 0:
            pointer = 1
            start = self.packets[0]
            last = self.packets[0]
            while pointer < count:
                current = self.packets[pointer]
                pointer += 1
                diff = current - last
                if diff == 1:
                    last = current
                elif diff > 1:
                    if start == last:
                        self.putByte(1)
                        self.putLTriad(start)
                        start = last = current
                    else:
                        self.putByte(0)
                        self.putLTriad(start)
                        self.putLTriad(last)
                        start = last = current
                    records += 1
            
        
    def decodePayload(self):
        pass
        
