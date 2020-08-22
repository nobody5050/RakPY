from struct import pack, unpack, calcsize 
import sys

class BinUtils:
    @staticmethod
    def readByte(data: bytes) -> int:
        return unpack('>b', data)[0]

    @staticmethod
    def writeByte(value: int) -> bytes:
        return pack('>b', data)

    @staticmethod
    def readLong(data: bytes) -> int:
        return unpack('>q', data)[0]
    
    @staticmethod
    def writeLong(value: int) -> bytes:
        return pack('>q', value)

    @staticmethod
    def readShort(data: bytes) -> int:
        return unpack('>h', data)[0]

    @staticmethod
    def writeShort(value: int) -> bytes:
        return pack('>h', value)

    @staticmethod
    def readUShort(data: bytes) -> int:
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
        return unpack('<L', data + b'\x00')[0]

    @staticmethod
    def writeUInt24LE(value: int) -> bytes:
        return pack('<L', value)[0:-1]
