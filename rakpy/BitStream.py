from struct import pack, unpack, calcsize 
import sys

from rakpy.RakPY import RakPY

class BitStream:
    offset = 0
    buffer = b""
    
    @staticmethod
    def reset():
        BinaryStream.buffer = b""
        BinaryStream.offset = 0
       
    @staticmethod
    def rewind():
        BinaryStream.offset = 0
       
    @staticmethod
    def setOffset(offset: int):
        BinaryStream.offset = offset
      
    @staticmethod
    def setBuffer(buffer: bytes = b"", offset: int = 0):
        BinaryStream.buffer = buffer
        BinaryStream.offset = offset
        
    @staticmethod
    def getOffset() -> int:
        return BinaryStream.offset
      
    @staticmethod
    def getBuffer() -> bytes:
        return BinaryStream.buffer
       
    @staticmethod
    def get(length) -> bytes:
        if length == 0:
            return b""
        buflength = len(BinaryStream.buffer)
        if length == True:
            s = BinaryStream.buffer[BinaryStream.offset:]
            BinaryStream.offset = buflength
            return s
        if length < 0:
            BinaryStream.offset = buflength - 1
            return b""
        remaining = buflength - BinaryStream.offset
        if remaining < length:
            raise Exception("Not enough bytes left in buffer: need " + str(length) + ", have " + str(remaining))
        if length == 1:
            b = BinaryStream.buffer[BinaryStream.offset]
            BinaryStream.offset += 1
            return b
        else:
            start = BinaryStream.offset - length
            BinaryStream.offset += length
            if start < 0:
                 start = start + len(BinaryStream.buffer)
            return BinaryStream.buffer[start:start + length]
       
    @staticmethod
    def getRemaining() -> str:
        s = BinaryStream.buffer[BinaryStream.offset:]
        if s == False:
            raise Exception("No bytes left to read")
        BinaryStream.offset = len(BinaryStream.buffer)
        return s
    
    @staticmethod
    def put(s):
        BinaryStream.buffer += s
    
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
    
    @staticmethod
    def getByte():
        return BitStream.readByte(BitStream.get(1))
     
    @staticmethod
    def putByte(value):
        BitStream.buffer += BitStream.writeByte(value)
    
    @staticmethod
    def getLong():
        return BitStream.readLong(BitStream.get(8))
     
    @staticmethod
    def putLong(value):
        BitStream.buffer += BitStream.writeLong(value)
        
    @staticmethod
    def getShort():
        return BitStream.readShort(BitStream.get(2))
     
    @staticmethod
    def putShort(value):
        BitStream.buffer += BitStream.writeShort(value)
        
    @staticmethod
    def getUShort():
        return BitStream.readUShort(BitStream.get(2))
     
    @staticmethod
    def putUShort(value):
        BitStream.buffer += BitStream.writeUShort(value)
     
    @staticmethod
    def getString() -> bytes:
        return BitStream.get(BitStream.getShort())
    
    @staticmethod
    def putString(value: bytes):
        BitStream.putShort(len(s))
        BitStream.put(s)

    @staticmethod
    def getBool():
        return BitStream.readBool(BitStream.get(1))
    
    @staticmethod
    def putBool(value):
        BitStream.buffer += BitStream.writeBool(value)
       
    @staticmethod
    def getAddress():
        version = BitStream.getByte()
        if version == 4: 
            ip = str((~BitStream.getByte()) & 0xff) + "." + str((~BitStream.getByte()) & 0xff) + "." + str((~BitStream.getByte()) & 0xff) + str((~BitStream.getByte()) & 0xff)
            port = BitStream.getUShort()
            return (ip, port, version)
        else:
            raise Exception("Unknown ip version " + str(version))
            
    @staticmethod
    def putAddress(ip: str, port: int, version: int = 4):
        BitStream.putByte(version)
        if version == 4:
            for s in str(ip).split("."):
                BitStream.putByte(int(s) & 0xff)
            BitStream.putUShort(port)
    
    @staticmethod
    def getUInt24LE():
        return BitStream.readUInt24LE(BitStream.get(3))
    
    @staticmethod
    def putUInt24LE(value):
        BitStream.buffer += BitStream.writeUInt24LE(value)
        
    @staticmethod
    def feof():
        try:
            BinaryStream.buffer[BinaryStream.offset]
            return True
        except:
            return False
