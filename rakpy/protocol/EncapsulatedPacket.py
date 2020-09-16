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
        packet = EncapsulatedPacket()
        header = buffer[0]
        packet.reliability = (header & 224) >> 5
        packet.split = (header & BitFlags.Split) > 0
        length = buffer[1:3]
        length >>= 3
        if length == 0:
            raise Exception("Got an empty encapsulated packet")
