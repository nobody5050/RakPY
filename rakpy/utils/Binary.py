from struct import pack, unpack, calcsize 
import sys

class Binary:
    @staticmethod
    def checkLength(data: bytes, expect: int):
        length = len(data)
        assert (length == expect), 'Expected ' + str(expect) + 'bytes, got ' + str(length)

    @staticmethod
    def readByte(data: bytes) -> int:
        Binary.checkLength(data, 1)
        return ord(data)

    @staticmethod
    def writeByte(value: int) -> bytes:
        return chr(value).encode()


    @staticmethod
    def readLong(data: bytes) -> int:
        Binary.checkLength(data, 8)
        return unpack('>Q', data)[0]
    
    @staticmethod
    def writeLong(value: int) -> bytes:
        return pack('>Q', value)

    @staticmethod
    def readShort(data: bytes) -> int:
        Binary.checkLength(data, 2)
        return unpack('>h', data)[0]

    @staticmethod
    def writeShort(value: int) -> bytes:
        Binary.checkLength(data, 2)
        return pack('>h', value)

    @staticmethod
    def readUnsignedShort(data: bytes) -> int:
        Binary.checkLength(data, 2)
        return unpack('>H', data)[0]

    @staticmethod
    def writeUnsignedShort(value: int) -> bytes:
        return pack('>H', value)
