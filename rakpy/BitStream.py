from struct import pack, unpack, calcsize 
import sys

from rakpy.RakPY import RakPY

class BitStream:
    offset = 0
    buffer = b""
    
    @staticmethod
    def reset():
        BitStream.buffer = b""
        BitStream.offset = 0
       
    @staticmethod
    def rewind():
        BitStream.offset = 0
       
    @staticmethod
    def setOffset(offset: int):
        BitStream.offset = offset
      
    @staticmethod
    def setBuffer(buffer: bytes = b"", offset: int = 0):
        BitStream.buffer = buffer
        BitStream.offset = offset
        
    @staticmethod
    def getOffset() -> int:
        return BitStream.offset
      
    @staticmethod
    def getBuffer() -> bytes:
        return BitStream.buffer
       
    @staticmethod
    def get(length) -> bytes:
        if length == 0:
            return b""
        buflength = len(BitStream.buffer)
        if length == True:
            s = BitStream.buffer[BitStream.offset:]
            BitStream.offset = buflength
            return s
        if length < 0:
            BitStream.offset = buflength - 1
            return b""
        remaining = buflength - BitStream.offset
        if remaining < length:
            raise Exception("Not enough bytes left in buffer: need " + str(length) + ", have " + str(remaining))
        if length == 1:
            b = BitStream.buffer[BitStream.offset]
            BitStream.offset += 1
            return b
        else:
            start = BitStream.offset - length
            BitStream.offset += length
            if start < 0:
                 start = start + len(BitStream.buffer)
            return BitStream.buffer[start:start + length]
       
    @staticmethod
    def getRemaining() -> str:
        s = BitStream.buffer[BitStream.offset:]
        if s == False:
            raise Exception("No bytes left to read")
        BitStream.offset = len(BitStream.buffer)
        return s
    
    @staticmethod
    def put(s):
        BitStream.buffer += s
    
    @staticmethod
    def readByte(data: bytes) -> int:
        return unpack('>b', data)[0]

    @staticmethod
    def writeByte(value: int) -> bytes:
        return pack('>b', value)

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
        BitStream.put(BitStream.writeLong(value))
        
    @staticmethod
    def getMagic():
        return self.get(16)
    
    @staticmethod
    def putMagic():
        BitStream.put(RakPY.MAGIC)
        
    @staticmethod
    def getShort():
        return BitStream.readShort(BitStream.get(2))
     
    @staticmethod
    def putShort(value):
        BitStream.put(BitStream.writeShort(value))
        
    @staticmethod
    def getUShort():
        return BitStream.readUShort(BitStream.get(2))
     
    @staticmethod
    def putUShort(value):
        BitStream.put(BitStream.writeUShort(value))
     
    @staticmethod
    def getString() -> bytes:
        return BitStream.get(BitStream.getShort())
    
    @staticmethod
    def putString(value: bytes):
        BitStream.putShort(len(value))
        BitStream.put(value)

    @staticmethod
    def getBool():
        return BitStream.readBool(BitStream.get(1))
    
    @staticmethod
    def putBool(value):
        BitStream.put(BitStream.writeBool(value))
       
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
        BitStream.put(BitStream.writeUInt24LE(value))
        
    @staticmethod
    def feof():
        try:
            BitStream.buffer[BitStream.offset]
            return True
        except:
            return False
