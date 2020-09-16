from binutilspy.Binary import Binary
from rakpy.protocol.BitFlags import BitFlags
from rakpy.protocol.Reliability import Reliability

class EncapsulatedPacket:
    buffer = b""
    reliability = None
    messageIndex = None
    sequenceIndex = None
    orderIndex = None
    orderChannel = None
    split = None
    splitCount = None
    splitIndex = None
    splitID = None
    needAck = False
    identifierAck = None
    
    def fromBinary(self, buffer):
        offset = 0
        packet = EncapsulatedPacket()
        header = Binary.readByte(buffer[offset])
        offset += 1
        packet.reliability = (header & 224) >> 5
        packet.split = (header & BitFlags.Split) > 0
        length = Binary.readShort(buffer[offset:offset + 2])
        length >>= 3
        offset += 2
        if length == 0:
            raise Exception("Got an empty encapsulated packet")
        if Reliability.isReliable(packet.reliability):
            packet.messageIndex = Binary.readLTriad(buffer[offset:offset + 3])
            offset += 3
        if Reliability.isSequenced(packet.reliability):
            packet.sequenceIndex = Binary.readLTriad(buffer[offset:offset + 3])
            offset += 3
