from binutilspy.Binary import Binary
from rakpy.protocol.Packet import Packet
from rakpy.protocol.PacketIdentifiers import PacketIdentifiers

class AcknowledgePacket(Packet):
    packets = []
    
    def encodePayload(self):
        payload = b""
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
                        payload += Binary.writeByte(1)
                        payload += Binary.writeLTriad(start)
                        start = last = current
                    else:
                        payload += Binary.writeByte(0)
                        payload += Binary.writeLTriad(start)
                        payload += Binary.writeLTriad(last)
                        start = last = current
                    records += 1
            pass
            
        
    def decodePayload(self):
        pass
        
