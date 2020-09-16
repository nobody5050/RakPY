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
