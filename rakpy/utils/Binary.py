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
        return unpack('>b', data)[0]

    @staticmethod
    def writeByte(value: int) -> bytes:
        return pack('>b', data)

    @staticmethod
    def readLong(data: bytes) -> int:
        Binary.checkLength(data, 8)
        return unpack('>q', data)[0]
    
    @staticmethod
    def writeLong(value: int) -> bytes:
        return pack('>q', value)

    @staticmethod
    def readShort(data: bytes) -> int:
        Binary.checkLength(data, 2)
        return unpack('>h', data)[0]

    @staticmethod
    def writeShort(value: int) -> bytes:
        Binary.checkLength(data, 2)
        return pack('>h', value)

    @staticmethod
    def readUShort(data: bytes) -> int:
        Binary.checkLength(data, 2)
        return unpack('>H', data)[0]

    @staticmethod
    def writeUShort(value: int) -> bytes:
        return pack('>H', value)
    
    @staticmethod
    def readBool(data: bytes) -> bool:
        return unpack('?', data)[0]

    @staticmethod
    def writeBool(value: bool) -> bytes:
        return b'\x01' if value else b'\x00'
    
    @staticmethod
    def readUInt24LE(data: bytes) -> int:
        Binary.checkLength(data, 3)
        return unpack('<L', data + b'\x00')[0]

    @staticmethod
    def writeUInt24LE(value: int) -> bytes:
        return pack('<L', value)[0:-1]
